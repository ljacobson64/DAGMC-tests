import argparse
import os
import sys
from subprocess import call
import multiprocessing as mp

class dagmc_test:
    def __init__(self, name, args):
        self.name = name
        self.exe = 'run.sh'

        self.dirs = {}
        self.inputs = {}
        self.outputs = {}
        self.other = {}

        self.physics = None    # mcnp5, mcnp6, or fluka
        self.run_type = None   # native or dagmc

        # DAG-MCNP only
        self.dirs['input'] = 'Inputs_dagmc'
        self.dirs['input_m2c'] = 'Inputs_mcnp2cad'
        self.dirs['sat'] = 'Geom_sat'
        self.dirs['gcad'] = 'Geom_h5m'
        self.dirs['result'] = os.path.join('Results', self.name)
        self.dirs['temp'] = os.path.join('Templates', self.name)
        self.inputs['gcad'] = self.name + '.h5m'
        self.other['sat'] = self.name + '.sat'
        self.flags = []
        self.meshes = []
        self.depends = []
        self.mpi_jobs = None

        # FluDag only
        self.geom_type = None  # usrtrack, usrbdx, or code
        self.num_runs = None

    def __repr__(self):
        return ('<dagmc_test ' + str(self.name) + '>')

    def __str__(self):
        return str(self.__dict__) + '\n'

    # Run mcnp2cad on a MCNP input file
    def run_mcnp2cad(self, mergetol = 1e-4):
        inp_file = os.path.join(self.dirs['input_m2c'], self.inputs['inp'])
        sat_file = os.path.join(self.dirs['sat'], self.other['sat'])

        call_shell('mkdir -p ' + self.dirs['sat'])
        call_shell('mcnp2cad ' + inp_file + ' -o ' + sat_file +
                   ' --geomver=1902' + ' --tol=' + str(mergetol))

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = 1e-4):
        sat_file = os.path.join(self.dirs['sat'], self.other['sat'])
        gcad_file = os.path.join(self.dirs['gcad'], self.inputs['gcad'])

        call_shell('mkdir -p ' + self.dirs['gcad'])
        call_shell('dagmc_preproc ' + sat_file + ' -o ' + gcad_file +
                   ' -f ' + str(ftol))

    # Setup results directory
    def setup_result_dir(self):
        call_shell('mkdir -p ' + self.dirs['result'])
        call_shell('rm -f ' + self.dirs['result'] + '/*')

        # Inputs
        for key, val in self.inputs.items():
            if key in self.dirs:
                link_orig = os.path.join('../..', self.dirs[key], val)
            else:
                link_orig = os.path.join('../..', self.dirs['input'], val)
            link_new = os.path.join(self.dirs['result'], val)
            call_shell('ln -snf ' + link_orig + ' ' + link_new)

        # Meshes (DAG-MCNP only)
        for mesh in self.meshes:
            link_orig = os.path.join('../..', self.dirs['input'], mesh)
            link_new = os.path.join(self.dirs['result'], mesh)
            call_shell('ln -snf ' + link_orig + ' ' + link_new)

        # Dependencies on results of other tests (DAG-MCNP only)
        for depend in self.depends:
            if depend[1] == 'rssa':
                depend_inp = 'wssa'
            else:
                depend_inp = depend[1]
            link_orig = os.path.join('..', depend[0], depend_inp)
            link_new = os.path.join(self.dirs['result'], depend[1] + '_' + depend[0])
            call_shell('ln -snf ' + link_orig + ' ' + link_new)

        # Other files (DAG-MCNP only)
        for key, val in self.other.items():
            if key == 'sat':
                continue
            link_orig = os.path.join('../..', self.dirs[key], val)
            link_new = os.path.join(self.dirs['result'], val)
            call_shell('ln -snf ' + link_orig + ' ' + link_new)

        # FLUKA process file (FluDAG only)
        if self.physics == 'fluka':
            writer = open(os.path.join(self.dirs['result'], 'process'), 'w')
            for i in range(1, self.num_runs + 1):
                writer.write(self.name + str(i).zfill(3) + '_fort.21\n')
            writer.write('\n' + self.name + '\n')
            writer.close()

        # Execution script
        exe_strs = ['']*2
        if self.physics == 'mcnp5' or self.physics == 'mcnp6':
            if self.mpi_jobs > 1:
                exe_strs[0] += ' mpiexec -np ' + str(self.mpi_jobs)
            exe_strs[0] += ' ' + self.physics + '.mpi'
            for flag in self.flags:
                exe_strs[0] += ' ' + flag
            for key, val in self.inputs.items():
                exe_strs[0] += ' ' + key + '=' + val
            for depend in self.depends:
                exe_strs[0] += ' ' + depend[1] + '=' + depend[1] + '_' + depend[0]
            exe_strs[1] += 'rm -f fcad runtpe srctp'
        elif self.physics == 'fluka':
            if self.run_type != 'code':
                exe_strs[0] += (' $FLUPRO/flutil/rfluka -N0 -M' +
                                str(self.num_runs))
                if self.geom_type == 'dagmc':
                    exe_strs[0] += (' -e $FLUDAG/mainfludag -d ' +
                                    os.path.join('../..', self.dirs['gcad'],
                                                 self.inputs['gcad']))
                exe_strs[0] += ' ' + self.inputs['inp']
            if self.run_type == 'usrtrack':
                exe_strs[1] += '$FLUPRO/flutil/ustsuw < process'
            elif self.run_type == 'usrbdx':
                exe_strs[1] += '$FLUPRO/flutil/usxsuw < process'
        exe_strs[0] = exe_strs[0].strip()
        exe_strs[1] = exe_strs[1].strip()
        with open(os.path.join(self.dirs['result'], self.exe), 'wb') as writer:
            writer.write('#!/bin/bash\n\n')
            for line in exe_strs:
                writer.write(line + '\n')
        call_shell('chmod +x ' + os.path.join(self.dirs['result'], self.exe))

    # Run the physics code
    def run_physics(self):
        # Run the code
        os.chdir(os.path.join(self.dirs['orig'], self.dirs['result']))
        call_shell('bash ' + self.exe, 'screen_out', 'screen_err', False)
        os.chdir(self.dirs['orig'])

        # Diff against the template
        for key, val in self.outputs.items():
            result = os.path.join(self.dirs['result'], val)
            template = os.path.join(self.dirs['temp'], val)
            diff = os.path.join(self.dirs['result'], 'diff_' + key)
            call_shell('diff ' + result + ' ' + template, diff)

    # Copy results to template directory
    def copy_results(self):
        call_shell('mkdir -p ' + self.dirs['temp'])
        for key, val in self.outputs.items():
            result = os.path.join(self.dirs['result'], val)
            template = os.path.join(self.dirs['temp'], val)
            call_shell('cp -f ' + result + ' ' + template)

    # Perform all steps required for the test
    def run_test(self, args):
        os.chdir(self.dirs['orig'])
        if args.mcnp2cad:
            self.run_mcnp2cad()
        if args.dagmc_preproc:
            self.run_dagmc_preproc()
        if args.setup:
            self.setup_result_dir()
        if args.run:
            self.run_physics()
        if args.copy:
            self.copy_results()

# Needed to make pool.apply_async() work
def run_test_external(test, args):
    test.run_test(args)

# Run all the tests
def run_multiple_tests(names, tests, args):
    if args.mpi:
        for name in names:
            test = tests[name]
            test.mpi_jobs = args.jobs
        jobs_serial = 1
    else:
        jobs_serial = args.jobs

    if jobs_serial > 1:
        pool = mp.Pool(processes = jobs_serial)

    for i, name in enumerate(names):
        test = tests[i]
        if jobs_serial > 1:
            pool.apply_async(run_test_external, args = (test, args))
        else:
            test.run_test(args)

    if jobs_serial > 1:
        pool.close()
        pool.join()

# Parse command line arguments
def parse_args(run_multiple_suites = False, only_print_help = False):
    parser = argparse.ArgumentParser(description =
                                     'Setup and/or run MCNP tests.')
    if run_multiple_suites:  # run_multiple.py
        parser.add_argument('suites', nargs = '*', default = 'all',
                            help = 'suites to process (default: all)')
    else:  # run_tests.py
        parser.add_argument('tests', nargs = '*', default = 'all',
                            help = 'tests to process (default: all)')
    parser.add_argument('-m', '--mcnp2cad', action = 'store_true',
                        help = 'run mcnp2cad')
    parser.add_argument('-d', '--dagmc_preproc', action = 'store_true',
                        help = 'run dagmc_preproc')
    parser.add_argument('-s', '--setup', action = 'store_true',
                        help = 'setup result directories')
    parser.add_argument('-r', '--run', action = 'store_true',
                        help = 'run physics code')
    parser.add_argument('-c', '--copy', action = 'store_true',
                        help = 'copy results to template directory')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    parser.add_argument('--mpi', action = 'store_true',
                        help = 'run DAG-MCNP in MPI mode')
    args = parser.parse_args()

    if only_print_help:
        parser.print_help()
        sys.exit(1)

    return args

# Call a shell command
def call_shell(string, stdout = '', stderr = '', append = False):
    print string
    if append:
        astr = '-a '
    else:
        astr = ''
    if stdout == '' and stderr == '':  # neither to file
        call_string = string
    elif stderr == '':  # stdout to file
        call_string = string + ' | tee ' + astr + stdout
    elif stdout == '':  # stderr to file
        call_string = string + ' 3>&1 1>&2 2>&3 | tee ' + astr + stderr
    elif stdout == stderr:  # both to same file
        call_string = string + ' 2>&1 | tee ' + astr + stdout
    else:  # each to different files
        call_string = ('(' + string + ' | tee ' + astr + stdout +
                       ') 3>&1 1>&2 2>&3 | tee ' + astr + stderr)
    call(call_string, shell = True)
