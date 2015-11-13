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
    tests[name] = mt.mcnp_test(name)
    test = tests[name]

    test.dirs["orig"] = current_dir

    test.inputs["inp"] = "inp" + test.name
    test.dirs["xsdir"] = "../xsec_data"
    test.inputs["xsdir"] = "testdir1"
    test.other["xslib"] = "testlib1"

    if test.name in ["01", "02", "07", "11", "12", "18", "19", "20", "21",
                     "22", "23", "26", "30", "77", "89"]:
        test.flags.append("fatal")
    if test.name in ["08", "10", "93"]:
        test.inputs["wwinp"] = "wwinp" + test.name
    if test.name == "26":
        test.flags.append("CN")
    if test.name in ["62"]:
        test.inputs["lcad"] = "lcad" + test.name
        test.flags.append("i")

    if test.name == "08":
        test.depends.append(["07", "rssa"])
    if test.name == "22":
        test.depends.append(["21", "rssa"])
    if test.name == "26":
        test.depends.append(["09", "rssa"])
        test.depends.append(["09", "runtpe"])
    if test.name == "27":
        test.depends.append(["09", "rssa"])
    if test.name == "29":
        test.depends.append(["07", "rssa"])
    if test.name == "34":
        test.depends.append(["33", "rssa"])

mt.run_multiple_tests(names_to_run, tests, args)
