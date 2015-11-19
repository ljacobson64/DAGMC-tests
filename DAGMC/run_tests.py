import os, sys, inspect

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mcnp_testing as mt

args = mt.parse_args()

names = range(1, 16);
for i, name in enumerate(names):
    names[i] = str(name).zfill(2)

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
    test.inputs["inp"] = "inp" + test.name
    test.inputs["gcad"] = "geom_" + test.name + ".h5m"
    test.other["sat"] = "geom_" + test.name + ".sat"

    # Common output
    test.outputs["outp"] = "outp"
    test.outputs["mctal"] = "mctal"

mt.run_multiple_tests(names_to_run, tests, args)
