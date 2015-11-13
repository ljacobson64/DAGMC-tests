import os, sys, inspect

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mcnp_testing as mt

args = mt.parse_args()

names = ["FLAT25", "GODIVA", "ICT2C3", "JEZ233", "LST2C2", "PNL2", "PUSH2O",
         "STACY36", "UH3C6", "ZEUS2", "BIGTEN", "FLATPU", "GODIVR", "IMF03",
         "JEZ240", "ORNL10", "PNL33", "SB25", "THOR", "UMF5C2", "FLAT23",
         "FLSTF1", "HISHPG", "IMF04", "JEZPU", "ORNL11", "PUBTNS", "SB5RN3",
         "TT2C11", "ZEBR8H"]

if args.tests == "all":
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = mt.mcnp_test(name)
    test = tests[name]

    test.dirs["orig"] = current_dir

    test.inputs["inp"] = test.name + "i"

mt.run_multiple_tests(names_to_run, tests, args)
