import argparse
import os
import sys
from subprocess import call
import multiprocessing as mp

class fluka_test:
    def __init__(self, name, args):
        self.name = name

        self.dirs = {}
        self.inputs = {}
        self.outputs = {}
        self.other = {}
        self.logs = {}
        self.runtypes = []
        self.numruns = None

    def __repr__(self):
        return ('Name: ' + str(self.name))

    def __str__(self):
        return str(self.__dict__) + '\n'

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = '1e-4'):
        if (('sat' not in self.dirs) or ('sat' not in self.other) or
            ('gcad' not in self.dirs) or ('gcad' not in self.inputs) or
            ('log' not in self.dirs) or ('gcad' not in self.logs)):
            return

        satfile = os.path.join(self.dirs['sat'], self.other['sat'])
        gcadfile = os.path.join(self.dirs['gcad'], self.inputs['gcad'])
        logfile = os.path.join(self.dirs['log'], self.logs['gcad'])

        call_shell('mkdir -p ' + self.dirs['gcad'])
        call_shell('mkdir -p ' + self.dirs['log'])
        call_shell('dagmc_preproc ' + satfile + ' -o ' + gcadfile + ' -f ' +
                   str(ftol), logfile)

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

        # Write FLUKA process file
        writer = open(os.path.join(self.dirs['result'], 'process'), 'w')
        for i in range(1, self.numruns + 1):
            writer.write(self.name + str(i).zfill(3) + '_fort.21\n')
        writer.write('\n' + self.name + '\n')
        writer.close()
    
    # Run FLUKA
    def run_fluka(self):
        # FLUKA execution string
        if self.runtypes[1] == 'code':
            run_fluka_str = ''
        else:
            run_fluka_str = ('$FLUPRO/flutil/rfluka -N0 -M' +
                             str(self.numruns))
            if self.runtypes[0] == 'native':
                pass
            elif self.runtypes[0] == 'dagmc':
                run_fluka_str += (' -e $FLUDAG/mainfludag -d ' +
                                  os.path.join('../..', self.dirs['gcad'],
                                               self.inputs['gcad']))
            run_fluka_str += ' ' + self.inputs['inp']
        if self.runtypes[1] == 'usrtrack':
            process_fluka_str = '$FLUPRO/flutil/ustsuw < process'
        elif self.runtypes[1] == 'usrbdx':
            process_fluka_str = '$FLUPRO/flutil/usxsuw < process'
        else:
            process_fluka_str = ''

        # Run FLUKA
        os.chdir(self.dirs['result'])
        call_shell(run_fluka_str, 'screen_out', 'screen_err')
        call_shell(process_fluka_str, 'screen_out_p', 'screen_err_p')
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
        # Run dagmc_preproc on an ACIS file
        if args.dagmc_preproc:
            self.run_dagmc_preproc()

        # Setup results directory
        if args.setup_dirs:
            self.setup_result_dir()

        # Run FLUKA
        if args.run_fluka:
            self.run_fluka()

        # Copy results to template directory
        if args.copy_results:
            self.copy_results()

# Needed to make pool.apply_async work
def run_test_external(test, args):
    test.run_test(args)

# Run all the passed tests
def run_multiple_tests(names, tests, args):
    jobs_serial = args.jobs

    if jobs_serial > 1:
        pool = mp.Pool(processes = jobs_serial)

    for name in names:
        test = tests[name]
        if jobs_serial > 1:
            pool.apply_async(run_test_external, args = (test, args))
        else:
            test.run_test(args)

    if jobs_serial > 1:
        pool.close()
        pool.join()

# Parse command line arguments
def parse_args():
    parser = argparse.ArgumentParser(description =
                                     'Setup and/or run MCNP tests.')
    parser.add_argument('tests', nargs = '*', default = 'all',
                        help = 'tests to process (default: all)')
    parser.add_argument('-d', '--dagmc_preproc', action = 'store_true',
                        help = 'run dagmc_preproc')
    parser.add_argument('-s', '--setup_dirs', action = 'store_true',
                        help = 'setup result directories')
    parser.add_argument('-r', '--run_fluka', action = 'store_true',
                        help = 'run FLUKA')
    parser.add_argument('-c', '--copy_results', action = 'store_true',
                        help = 'copy results to template directory')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    if (not args.dagmc_preproc and not args.setup_dirs and not args.run_fluka
        and not args.copy_results):
        parser.print_help()
        sys.exit(1)
    return args

# Call a shell command
def call_shell(string, stdout = '', stderr = ''):
    print string
    #'''
    if stdout == '' and stderr == '':  # neither to file
        call(string, shell = True)
    elif stderr == '':  # stdout to file
        call(string + ' | tee ' + stdout, shell = True)
    elif stdout == '':  # stderr to file
        call(string + ' 3>&1 1>&2 2>&3 | tee ' + stderr, shell = True)
    elif stdout == stderr:  # both to same file
        call(string + ' 2>&1 | tee ' + stdout, shell = True)
    else:  # both to different files
        call('(' + string + ' | tee ' + stdout +
             ') 3>&1 1>&2 2>&3 | tee ' + stderr, shell = True)
    #'''
