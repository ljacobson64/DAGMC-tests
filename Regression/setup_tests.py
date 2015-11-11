from subprocess import call
import os

def call_shell(string):
    print string
    call(string, shell = True)

class mcnp_test:
    def __init__(self, test_id):
        self.input_nat_dir = "Inputs_native"
        self.input_dag_dir = "Inputs_dagmc"
        self.sat_dir = "Geom_sat"
        self.h5m_dir = "Geom_h5m"
        self.log_dir = "Logs"
        self.result_dir = "Results/" + test_id
        
        self.inp = "inp" + test_id
        self.sat = "geom" + test_id + ".sat"
        self.h5m = "geom" + test_id + ".h5m"
        
        self.satlog = "geom" + test_id + ".sat.log"
        self.h5mlog = "geom" + test_id + ".h5m.log"
        
        self.xsdir_dir = ""
        self.xsdir = ""
        self.options = ""
        
        self.geomver = "1902"
        self.ftol = "1e-4"

    def __repr__(self):
        return "inp: " + self.inp

    def __str__(self):
        return "inp: " + self.inp

    def strip_geom_from_inp(self):
        reader = open(os.path.join(self.input_nat_dir, self.inp), 'r')
        lines = reader.readlines()
        reader.close()

        call_shell("mkdir -p " + self.input_dag_dir)
        writer = open(os.path.join(self.input_dag_dir, self.inp), 'w')
        writer.write(lines[0])
        num_blank_lines = 0
        for line in lines[1:]:
            if num_blank_lines < 2:
                writer.write("c " + line)
            else:
                writer.write(line)
            if line.strip() == "":
                num_blank_lines += 1
        writer.close()

    def run_mcnp2cad(self):
        call_shell("mkdir -p " + self.sat_dir)
        call_shell("mkdir -p " + self.log_dir)
        call_shell("mcnp2cad " + os.path.join(self.input_nat_dir, self.inp) +
                   " -o " + os.path.join(self.sat_dir, self.sat) +
                   " --geomver=" + self.geomver +
                   " 2>&1 | tee -a " + os.path.join(self.log_dir, self.satlog))

    def run_dagmc_preproc(self):
        call_shell("mkdir -p " + self.h5m_dir)
        call_shell("mkdir -p " + self.log_dir)
        call_shell("dagmc_preproc " + os.path.join(self.sat_dir, self.sat) +
                   " -o " + os.path.join(self.h5m_dir, self.h5m) +
                   " -f " + self.ftol +
                   " 2>&1 | tee -a " + os.path.join(self.log_dir, self.h5mlog))

    def setup_result_dir(self):
        call_shell("mkdir -p " + self.result_dir)
        call_shell("ln -sf " + os.path.join("../..", self.input_dag_dir, self.inp) +
                   " " + os.path.join(self.result_dir, self.inp))
        call_shell("ln -sf " + os.path.join("../..", self.h5m_dir, self.h5m) +
                   " " + os.path.join(self.result_dir, self.h5m))
        call_shell("ln -sf " + os.path.join("../..", self.xsdir_dir, self.xsdir) +
                   " " + os.path.join(self.result_dir, self.xsdir))
        call_shell("ln -sf " + os.path.join("../..", self.xsdir_dir, self.xslib) +
                   " " + os.path.join(self.result_dir, self.xslib))

    def call_mcnp(self, prun, mcnp):
        call_mcnp_str = prun + " " + mcnp
        if self.inp != "":
            call_mcnp_str += " i=" + self.inp
        if self.h5m != "":
            call_mcnp_str += " g=" + self.h5m
        if self.xsdir != "":
            call_mcnp_str += " xsdir=" + self.xsdir
        call_mcnp_str += self.options
        call_shell(call_mcnp_str)

original_dir = os.getcwd()

#prun = "mpiexec -np 24"
prun = ""
mcnp = "mcnp5.mpi"

test_ids = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10",
            "11", "12", "13", "14", "15", "16", "17", "18", "19", "20",
            "21", "22", "23", "24", "25", "26", "27", "28", "29", "30",
            "31", "32", "33", "34", "35", "36", "37", "38", "39", "40",
            "41", "42", "47", "48", "77", "86", "89", "90", "93", "94",
            "95", "98", "99", "103", "104", "111", "112", "113", "114",
            "116", "118"]
test_ids_fatal = ["01", "02", "07", "11", "12", "18", "19", "20", "21", "23",
                  "30", "33", "77", "89"]

for test_id in [test_ids[0]]:
    test = mcnp_test(test_id)

    test.xsdir_dir = "../xsec_data"
    test.xsdir = "testdir1"
    test.xslib = "testlib1"
    if test_id in test_ids_fatal:
        test.options += " fatal"

    test.strip_geom_from_inp()

    test.setup_result_dir()

    test.run_mcnp2cad()
    test.run_dagmc_preproc()

    os.chdir(test.result_dir)
    test.call_mcnp(prun, mcnp)
    os.chdir(original_dir)
