import argparse, os, sys
from subprocess import call
import multiprocessing as mp

class mcnp_test:
    def __init__(self, name, args):
        self.name = name

        self.dirs = {}
        self.dirs["orig"] = ""
        self.dirs["input"] = "Inputs"
        self.dirs["sat"] = "Geom_sat"
        self.dirs["gcad"] = "Geom_h5m"
        self.dirs["log"] = "Logs"
        self.dirs["result"] = "Results/" + name

        self.inputs = {}
        self.inputs["gcad"] = "geom_" + name + ".h5m"

        self.other = {}
        self.other["sat"] = "geom_" + name + ".sat"

        self.logs = {}
        self.logs["gcad"] = "geom_" + name + ".h5m.log"

        self.cmds = {}
        if args.mpi:
            self.cmds["prefix"] = "mpiexec -np " + str(args.jobs)
        else:
            self.cmds["prefix"] = ""
        self.cmds["exe"] = "mcnp5.mpi"

        self.flags = []
        self.depends = []

    def __repr__(self):
        return ("Name: " + str(self.name))

    def __str__(self):
        return str(self.__dict__) + "\n"

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = "1e-4"):
        satfile = os.path.join(self.dirs["sat"], self.other["sat"])
        gcadfile = os.path.join(self.dirs["gcad"], self.inputs["gcad"])
        logfile = os.path.join(self.dirs["log"], self.logs["gcad"])

        call_shell("mkdir -p " + self.dirs["gcad"])
        call_shell("mkdir -p " + self.dirs["log"])
        call_shell("dagmc_preproc " + satfile + " -o " + gcadfile +
                   " -f " + str(ftol), logfile)

    # Setup results directory
    def setup_result_dir(self):
        call_shell("mkdir -p " + self.dirs["result"])
        call_shell("rm -f " + self.dirs["result"] + "/*")
        for key, val in self.inputs.items():
            if key in self.dirs:
                dir = os.path.join("../..", self.dirs[key])
            else:
                dir = os.path.join("../..", self.dirs["input"])
            call_shell("ln -sf " + os.path.join(dir, val) +
                       " " + os.path.join(self.dirs["result"], val))
        for depend in self.depends:
            if depend[1] == "rssa":
                depend_inp = "wssa"
            else:
                depend_inp = depend[1]
            dep_name = depend[1] + depend[0]
            dir = os.path.join("..", depend[0])
            call_shell("ln -sf " + os.path.join(dir, depend_inp) +
                       " " + os.path.join(self.dirs["result"], dep_name))
        if "xslib" in self.other:
            dir = os.path.join("../..", self.dirs["xsdir"])
            call_shell("ln -sf " + os.path.join(dir, self.other["xslib"]) +
                       " " + os.path.join(self.dirs["result"],
                       self.other["xslib"]))

    # Run MCNP
    def run_mcnp(self):
        run_mcnp_str = (self.cmds["prefix"] + " " + self.cmds["exe"])
        for flag in self.flags:
            run_mcnp_str += " " + flag
        for key, val in self.inputs.items():
            run_mcnp_str += " " + key + "=" + val
        for depend in self.depends:
            run_mcnp_str += " " + depend[1] + "=" + depend[1] + depend[0]
        run_mcnp_str = run_mcnp_str.strip()
        #print run_mcnp_str
        call_shell(run_mcnp_str, "screen_out", "screen_err")
        call_shell("rm -f fcad")

    # Perform all steps required for the test
    def run_test(self, args):
        # Run dagmc_preproc on an ACIS file
        if args.dagmc_preproc:
            self.run_dagmc_preproc("1e-4")

        # Setup results directory
        if args.setup_dirs:
            self.setup_result_dir()

        # Run MCNP
        if args.run_mcnp:
            os.chdir(self.dirs["result"])
            self.run_mcnp()
            os.chdir(self.dirs["orig"])

# Needed to make pool.apply_async work
def run_test_external(test, args):
    test.run_test(args)

# Run all the passed tests
def run_multiple_tests(names, tests, args):
    if args.mpi:
        jobs_serial = 1
    else:
        jobs_serial = args.jobs

    if jobs_serial > 1:
        pool = mp.Pool(processes = jobs_serial)

    for name in names:
        test = tests[name]
        if test.depends == []:
            if jobs_serial > 1:
                pool.apply_async(run_test_external, args = (test, args))
            else:
                test.run_test(args)
    for name in names:
        test = tests[name]
        if test.depends != []:
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
                                     "Setup and/or run MCNP tests.")
    parser.add_argument("tests", nargs = "*", default = "all",
                        help = "tests to process (default: all)")
    parser.add_argument("-d", "--dagmc_preproc", action="store_true",
                        help = "run dagmc_preproc")
    parser.add_argument("-s", "--setup_dirs", action="store_true",
                        help = "setup result directories")
    parser.add_argument("-r", "--run_mcnp", action="store_true",
                        help = "run MCNP")
    parser.add_argument("-j", "--jobs", type = int, default = 1,
                        help = "number of jobs")
    parser.add_argument("--mpi", action="store_true",
                        help = "run MCNP in MPI mode")
    args = parser.parse_args()
    if not args.dagmc_preproc and not args.setup_dirs and not args.run_mcnp:
        parser.print_help()
        sys.exit(1)
    return args

# Call a shell command
def call_shell(string, stdout = "", stderr = ""):
    print string
    if stdout == "" and stderr == "":  # neither to file
        call(string, shell = True)
    elif stderr == "":  # stdout to file
        call(string + " | tee " + stdout, shell = True)
    elif stdout == "":  # stderr to file
        call(string + " 3>&1 1>&2 2>&3 | tee " + stderr, shell = True)
    elif stdout == stderr:  # both to same file
        call(string + " 2>&1 | tee " + stdout, shell = True)
    else:  # both to different files
        call("(" + string + " | tee " + stdout +
             ") 3>&1 1>&2 2>&3 | tee " + stderr, shell = True)
