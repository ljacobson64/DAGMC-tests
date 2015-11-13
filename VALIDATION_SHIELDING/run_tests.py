import os, sys, inspect

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mcnp_testing as mt

args = mt.parse_args()

names = ["BE08", "C29", "CCR20", "COAIR", "COTEF", "FE09", "FS1ONN", "FS3OFN",
         "FS3ONP", "FS7OFP", "FS7ONN", "H2O19", "KERMIN", "LI616", "N31",
         "PB14", "SKYINP", "SMAIR", "SMTEF"]

tests = {}
for name in names:
    tests[name] = mt.mcnp_test(name)
    test = tests[name]

    test.dirs["orig"] = current_dir

    test.inputs["inp"] = test.name + "i"

mt.run_multiple_tests(names, tests, args.jobs)
