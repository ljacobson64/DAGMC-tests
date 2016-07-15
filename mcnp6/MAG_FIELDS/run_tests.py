import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15']

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
    test.inputs['inp'] = 'inp' + test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # MESHTAL output
    if test.name in ['01', '02', '05', '06', '08', '09', '10', '11', '13',
                     '14']:
        test.outputs['meshtal'] = 'meshtal'

dagtest.run_multiple_tests(names_to_run, tests, args)
