import os, sys, inspect

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import mcnp_testing as mt

args = mt.parse_args()

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

    # xsdir setup
    test.dirs["xsdir"] = "../xsec_data"
    test.inputs["xsdir"] = "testdir1"
    test.other["xslib"] = "testlib1"

    # Common input
    test.inputs["inp"] = "inp" + test.name
    test.inputs["gcad"] = "geom_" + test.name + ".h5m"
    test.other["sat"] = "geom_" + test.name + ".sat"

    # Common output
    test.outputs["outp"] = "outp"
    test.outputs["mctal"] = "mctal"

    # Flags
    if test.name in ["01", "02", "07", "11", "12", "18", "19", "20", "21",
                     "22", "23", "26", "30", "77", "89"]:
        test.flags.append("fatal")
    if test.name == "26":
        test.flags.append("CN")
    if test.name in ["62"]:
        test.flags.append("i")

    # Special input
    if test.name in ["08", "10", "93"]:
        test.inputs["wwinp"] = "wwinp" + test.name
    if test.name in ["62"]:
        test.inputs["lcad"] = "lcad" + test.name

    # Dependencies
    if test.name in ["08"]:
        test.depends.append(["07", "rssa"])
    if test.name in ["22"]:
        test.depends.append(["21", "rssa"])
    if test.name in ["27"]:
        test.depends.append(["09", "rssa"])
    if test.name in ["29"]:
        test.depends.append(["07", "rssa"])
    if test.name in ["34"]:
        test.depends.append(["33", "rssa"])
    if test.name in ["26"]:
        test.depends.append(["09", "wssa"])
        test.depends.append(["09", "runtpe"])

    # Special output
    if test.name in ["62"]:
        del test.outputs["mctal"]
    if test.name in ["39"]:
        test.outputs["meshtal"] = "meshtal"
    if test.name in ["08", "10", "12"]:
        test.outputs["wwout"] = "wwout"
    if test.name in ["08", "12"]:
        test.outputs["wwone"] = "wwone"
    if test.name in ["02", "03", "08", "23"]:
        test.outputs["ptrac"] = "ptrac"

mt.run_multiple_tests(names_to_run, tests, args)
if args.summary:
    mt.produce_summary(names_to_run, tests, args)
