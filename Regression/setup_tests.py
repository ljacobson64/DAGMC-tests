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

        self.dirs = {}
        self.dirs["orig"] = ""
        self.dirs["input"] = "Inputs"
        self.dirs["sat"] = "Geom_sat"
        self.dirs["h5m"] = "Geom_h5m"
        self.dirs["log"] = "Logs"
        self.dirs["xsdir"] = "../xsec_data"
        self.dirs["result"] = "Results/" + test_id

        self.inputs = {}
        self.inputs["inp"] = "inp" + test_id
        self.inputs["gcad"] = "geom" + test_id + ".h5m"
        self.inputs["xsdir"] = "testdir1"

        self.other = {}
        self.other["sat"] = "geom" + test_id + ".sat"
        self.other["xslib"] = "testlib1"

        self.logs = {}
        self.logs["h5m"] = "geom" + test_id + ".h5m.log"

        self.cmds = {}
        #self.cmd["pre"] = "mpiexec -np 24"
        self.cmds["pre"] = ""
        self.cmds["exe"] = "mcnp5.mpi"

        self.flags = []

    def __repr__(self):
        return "mcnp_test: " + self.id

    def __str__(self):
        return "mcnp_test: " + self.id

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = 1e-4):
        call_shell("mkdir -p " + self.dirs["h5m"])
        call_shell("mkdir -p " + self.dirs["log"])
        call_shell("dagmc_preproc " + os.path.join(self.dirs["sat"], self.other["sat"]) +
                   " -o " + os.path.join(self.dirs["h5m"], self.inputs["h5m"]) +
                   " -f " + str(ftol),
                   os.path.join(self.dirs["log"], self.logs["h5m"]))

    # Setup results directory
    def setup_result_dir(self):
        call_shell("mkdir -p " + self.dirs["result"])
        call_shell("rm -rf " + self.dirs["result"] + "/*")
        call_shell("ln -sf " + os.path.join("../..", self.dirs["input"], self.inputs["inp"]) +
                   " " + os.path.join(self.dirs["result"], self.inputs["inp"]))
        call_shell("ln -sf " + os.path.join("../..", self.dirs["h5m"], self.inputs["h5m"]) +
                   " " + os.path.join(self.dirs["result"], self.inputs["h5m"]))
        call_shell("ln -sf " + os.path.join("../..", self.dirs["xsdir"], self.inputs["xsdir"]) +
                   " " + os.path.join(self.dirs["result"], self.inputs["xsdir"]))
        call_shell("ln -sf " + os.path.join("../..", self.dirs["xsdir"], self.inputs["xsdir"]) +
                   " " + os.path.join(self.dirs["result"], self.other["xslib"]))

    # Run MCNP
    def run_mcnp(self):
        run_mcnp_str = self.cmds["pre"] + " " + self.cmds["exe"]
        for key, val in self.inputs.items():
            run_mcnp_str += " " + key + "=" + val
        for flag in self.flags:
            run_mcnp_str += " " + flag
        print run_mcnp_str
        #call_shell(run_mcnp_str, "screen_out", "screen_err")

def setup_test(test):
    # Run dagmc_preproc on an ACIS file
    #test.run_dagmc_preproc("1e-4")

    # Setup results directory
    #test.setup_result_dir()
    
    # Run MCNP
    os.chdir(test.dirs["result"])
    test.run_mcnp()
    os.chdir(test.dirs["orig"])

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
        test.dirs["orig"] = original_dir

        if test_id in test_ids_fatal:
            test.flags.append("fatal")

        pool.apply_async(setup_test, args=(test,))

    pool.close()
    pool.join()

main()
