import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['prob1_abs', 'prob1_sct', 'prob2_abs', 'prob2_sct', 'prob3_abs',
         'prob3_sct']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name + '.txt'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xs'] = 'Files'
    if test.name in ['prob1_abs', 'prob2_abs', 'prob3_abs']:
        test.other['xs'] = 'xs1.txt'
    if test.name in ['prob1_sct', 'prob2_sct', 'prob3_sct']:
        test.other['xs'] = 'xs2.txt'

dagtest.run_multiple_tests(names_to_run, tests, args)
