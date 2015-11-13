import argparse
from collections import OrderedDict
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
        self.name = test_id

        self.dirs = OrderedDict()
        self.dirs["orig"] = ""
        self.dirs["input"] = "Inputs"
        self.dirs["sat"] = "Geom_sat"
        self.dirs["gcad"] = "Geom_h5m"
        self.dirs["log"] = "Logs"
        self.dirs["result"] = "Results/" + test_id
        self.dirs["xsdir"] = "../xsec_data"

        self.inputs = OrderedDict()
        self.inputs["inp"] = "inp" + test_id
        self.inputs["gcad"] = "geom" + test_id + ".h5m"
        self.inputs["xsdir"] = "testdir1"

        self.other = OrderedDict()
        self.other["sat"] = "geom" + test_id + ".sat"
        self.other["xslib"] = "testlib1"

        self.logs = OrderedDict()
        self.logs["gcad"] = "geom" + test_id + ".h5m.log"

        self.cmds = OrderedDict()
        #self.cmd["pre"] = "mpiexec -np 24"
        self.cmds["prefix"] = ""
        self.cmds["exe"] = "mcnp5.mpi"
        self.cmds["suffix"] = ""

        self.flags = []
        self.depends = []

    def __repr__(self):
        return ("Name: " + str(self.name))

    def __str__(self):
        return str(self.__dict__) + "\n"

    # Run dagmc_preproc on an ACIS file
    def run_dagmc_preproc(self, ftol = 1e-4):
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
        run_mcnp_str = (self.cmds["prefix"] + " " + self.cmds["exe"] + " " +
                        self.cmds["suffix"])
        for key, val in self.inputs.items():
            run_mcnp_str += " " + key + "=" + val
        for depend in self.depends:
            run_mcnp_str += " " + depend[1] + "=" + depend[1] + depend[0]
        for flag in self.flags:
            run_mcnp_str += " " + flag
        #print run_mcnp_str
        call_shell(run_mcnp_str, "screen_out", "screen_err")

def setup_test(test):
    # Run dagmc_preproc on an ACIS file
    #test.run_dagmc_preproc("1e-4")

    # Setup results directory
    test.setup_result_dir()
    
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

    names = [ 1,  2,  3,  4,      6,  7,  8,  9, 10,
                 12,                         19, 20,
             21, 22, 23,         26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37,     39,    
             41, 42,                 47,            
             61, 62, 63, 64, 65, 66, 67, 68,        
                                 86,             90,
                     93, 94, 95,         98, 99    ]
    for i, name in enumerate(names):
        names[i] = str(name).zfill(2)

    jobs = args.jobs
    if jobs > 1:
        pool = mp.Pool(processes = jobs)

    tests = {}
    for name in names:
        tests[name] = mcnp_test(name)

    for name in names:
        test = tests[name]

        test.dirs["orig"] = original_dir

        if test.name in ["01", "02", "07", "11", "12", "18", "19", "20", "21",
                         "22", "23", "26", "30", "77", "89"]:
            test.flags.append("fatal")
        if test.name in ["08", "10", "93"]:
            test.inputs["wwinp"] = "wwinp" + test.name
        if test.name in ["62"]:
            test.inputs["lcad"] = "lcad" + test.name

        if test.name == "08":
            test.depends.append(["07", "rssa"])
        if test.name == "22":
            test.depends.append(["21", "rssa"])
        if test.name == "26":
            test.depends.append(["09", "rssa"])
            test.depends.append(["09", "runtpe"])
            test.flags.append("CN")
        if test.name == "27":
            test.depends.append(["09", "rssa"])
        if test.name == "29":
            test.depends.append(["07", "rssa"])
        if test.name == "34":
            test.depends.append(["33", "rssa"])
        if test.name == "62":
            test.flags.append("i")

    #for name in names:
    #    test = tests[name]
    #    if test.depends != []:
    #        continue
    #    if jobs > 1:
    #        pool.apply_async(setup_test, args=(test,))
    #    else:
    #        setup_test(test)
    for name in names:
        test = tests[name]
        if test.depends == []:
            continue
        if jobs > 1:
            pool.apply_async(setup_test, args=(test,))
        else:
            setup_test(test)

    if jobs > 1:
        pool.close()
        pool.join()

main()
