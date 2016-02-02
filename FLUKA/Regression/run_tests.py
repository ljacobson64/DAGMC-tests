import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import fluka_testing as ft

args = ft.parse_args()

names = [1, 2, 3, 11, 12, 13, 21, 22, 41, 42, 51, 52, 61, 62]
for i, name in enumerate(names):
    names[i] = 'test' + str(name).zfill(2)

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = ft.fluka_test(name, args)
    test = tests[name]

    # Run types
    if test.name in ['test41', 'test42']:
        test.runtype = 'usrbdx'
    elif test.name in ['test61', 'test62']:
        test.runtype = 'code'
    else:
        test.runtype = 'usrtrack'

    # Number of runs
    if test.name in ['test01', 'test61', 'test62']:
        test.numruns = 1
    else:
        test.numruns = 5

    # Directories
    test.dirs['orig'] = current_dir

    # Outputs
    if test.runtype != 'code':
        for i in range(test.numruns):
            istr = str(i).zfill(3)
            test.outputs['out' + istr] = test.name + istr + '.out'

ft.run_multiple_tests(names_to_run, tests, args)
