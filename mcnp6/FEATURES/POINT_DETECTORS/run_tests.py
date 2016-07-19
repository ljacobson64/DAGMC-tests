import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['case1', 'case2', 'case3', 'case4', 'case5', 'case6', 'case7', 'case8',
         'case9', 'case10', 'case11', 'case12', 'case13', 'case14', 'case15',
         'case16', 'case17', 'case18', 'case19', 'case20', 'case21', 'case22',
         'case23', 'case24', 'case25', 'case26', 'rotate1b', 'rotate1',
         'thermal1']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name + '.i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = '../../xsec_data'
    test.dirs['xslib'] = '../../xsec_data'
    test.inputs['xsdir'] = 'testdir1'
    test.other['xslib'] = 'testlib1'

    return test

def setup_tests(names, args):
    tests = []
    for name in names:
        tests.append(setup_test(name, args))
    return tests

args = dagtest.parse_args()

if __name__ != '__main__':
    args.tests = 'all'
if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = setup_tests(names_to_run, args)

if __name__ == '__main__':
    dagtest.run_multiple_tests(names_to_run, tests, args)
