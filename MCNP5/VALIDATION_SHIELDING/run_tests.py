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

if args.tests == "all":
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = mt.mcnp_test(name, args)
    test = tests[name]

    # Directories
    test.dirs["orig"] = current_dir
    test.dirs["input"] = "Inputs"
    test.dirs["sat"] = "Geom_sat"
    test.dirs["gcad"] = "Geom_h5m"

    # Common input
    test.inputs["inp"] = test.name + "i"
    test.inputs["gcad"] = "geom_" + test.name + ".h5m"
    test.other["sat"] = "geom_" + test.name + ".sat"

    # Common output
    test.outputs["outp"] = "outp"
    test.outputs["mctal"] = "mctal"

    # Special output
    if name in ["FS3OFN", "FS3ONP", "FS7OFP", "FS7ONN"]:
        test.outputs["wwout"] = "wwout"

mt.run_multiple_tests(names_to_run, tests, args)