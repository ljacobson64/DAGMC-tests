import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['case1a', 'case1b', 'case2a', 'case2b', 'case3a', 'case3b', 'case4a',
         'case4b', 'case5a', 'case5b', 'case6']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name + '.i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # C option
    if test.name in ['case2a', 'case2b']:
        test.flags.append('c')

    # Cross section data
    test.dirs['xsdir'] = '../../xsec_data'
    test.dirs['xslib'] = '../../xsec_data'
    if test.name not in ['case6']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'
    if test.name in ['case6']:
        test.inputs['xsdir'] = 'xsdir'

    # RUNTPE dependencies
    if test.name in ['case2a']:
        test.depends.append(['case1a', 'runtpe'])
    if test.name in ['case2b']:
        test.depends.append(['case1b', 'runtpe'])

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
