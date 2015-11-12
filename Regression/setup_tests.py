import argparse
from subprocess import call
import os
import multiprocessing as mp

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

class mcnp_test:
    def __init__(self, test_id):
        self.id = test_id

        self.input_dir = "Inputs"
        self.sat_dir = "Geom_sat"
        self.h5m_dir = "Geom_h5m"
        self.log_dir = "Logs"
        self.result_dir = "Results/" + test_id

        self.inp = "inp" + test_id
        self.sat = "geom" + test_id + ".sat"
        self.h5m = "geom" + test_id + ".h5m"

        self.h5mlog = "geom" + test_id + ".h5m.log"

        #mcnp.prun = "mpiexec -np 24"
        self.prun = ""
        self.mcnp = "mcnp5.mpi"

        self.orig_dir = ""
        self.xsdir_dir = ""
        self.xsdir = ""
        self.options = ""

    def __repr__(self):
        return "mcnp_test: " + self.id

    def __str__(self):
        return "mcnp_test: " + self.id

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = 1e-4):
        call_shell("mkdir -p " + self.h5m_dir)
        call_shell("mkdir -p " + self.log_dir)
        call_shell("dagmc_preproc " + os.path.join(self.sat_dir, self.sat) +
                   " -o " + os.path.join(self.h5m_dir, self.h5m) +
                   " -f " + str(ftol),
                   os.path.join(self.log_dir, self.h5mlog))

    # Setup results directory
    def setup_result_dir(self):
        call_shell("mkdir -p " + self.result_dir)
        call_shell("rm -rf " + self.result_dir + "/*")
        call_shell("ln -sf " + os.path.join("../..", self.input_dir, self.inp) +
                   " " + os.path.join(self.result_dir, self.inp))
        call_shell("ln -sf " + os.path.join("../..", self.h5m_dir, self.h5m) +
                   " " + os.path.join(self.result_dir, self.h5m))
        call_shell("ln -sf " + os.path.join("../..", self.xsdir_dir, self.xsdir) +
                   " " + os.path.join(self.result_dir, self.xsdir))
        call_shell("ln -sf " + os.path.join("../..", self.xsdir_dir, self.xslib) +
                   " " + os.path.join(self.result_dir, self.xslib))

    # Run MCNP
    def run_mcnp(self):
        run_mcnp_str = self.prun + " " + self.mcnp
        if self.inp != "":
            run_mcnp_str += " i=" + self.inp
        if self.h5m != "":
            run_mcnp_str += " g=" + self.h5m
        if self.xsdir != "":
            run_mcnp_str += " xsdir=" + self.xsdir
        run_mcnp_str += self.options
        print run_mcnp_str
        call_shell(run_mcnp_str, "screen_out", "screen_err")

def setup_test(test):
    # Run dagmc_preproc on an ACIS file
    test.run_dagmc_preproc("1e-4")

    # Setup results directory
    test.setup_result_dir()
    
    # Run MCNP
    os.chdir(test.result_dir)
    test.run_mcnp()
    os.chdir(test.orig_dir)

def main():
    parser = argparse.ArgumentParser(description = "Setup MCNP tests.")
    parser.add_argument("-j", "--jobs", type = int, default = 1,
                        help = "number of jobs")
    args = parser.parse_args()
    original_dir = os.getcwd()

    test_ids = [ 1,  2,  3,  4,      6,  7,  8,  9, 10,
                    12,                         19, 20,
                21, 22, 23,         26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37,     39,    
                41, 42,                 47,            
                61, 62, 63, 64, 65, 66, 67, 68,        
                                    86,             90,
                        93, 94, 95,         98, 99    ]
    test_ids_fatal = [1, 2, 7, 11, 12, 18, 19, 20, 21, 22, 23, 26, 30, 77, 89]

    for i, test_id in enumerate(test_ids):
        test_ids[i] = str(test_id).zfill(2)
    for i, test_id in enumerate(test_ids_fatal):
        test_ids_fatal[i] = str(test_id).zfill(2)

    jobs = args.jobs
    pool = mp.Pool(processes = jobs)
    for test_id in test_ids:
        test = mcnp_test(test_id)
        test.orig_dir = original_dir

        test.xsdir_dir = "../xsec_data"
        test.xsdir = "testdir1"
        test.xslib = "testlib1"
        if test_id in test_ids_fatal:
            test.options += " fatal"

        pool.apply_async(setup_test, args=(test,))

    pool.close()
    pool.join()

main()
