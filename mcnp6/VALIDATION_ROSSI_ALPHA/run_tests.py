import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['heu-met-fast-001', 'heu-met-fast-028', 'heu-met-fast-072-case-1',
         'heu-met-fast-073', 'heu-met-inter-006-case-1',
         'heu-met-inter-006-case-4', 'ieu-met-fast-007-case-4',
         'ieu-sol-therm-004-case-46', 'ieu-sol-therm-007-case-30',
         'pu-met-fast-001', 'pu-met-fast-006', 'pu-met-fast-008-case-2',
         'u233-met-fast-001', 'u233-met-fast-006']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name + 'i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = 'Files'
    test.inputs['xsdir'] = 'xsdir_endf7'

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
