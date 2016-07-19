import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = 'inp' + test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # FATAL option
    if test.name in ['17']:
        test.flags.append('fatal')

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.dirs['xslib'] = '../xsec_data'
    if test.name in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                     '11', '12']:
        test.inputs['xsdir'] = 'xsdirph'
    if test.name in ['13', '19']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'
    if test.name in ['14', '15', '16', '17', '18', '20', '21', '22']:
        test.inputs['xsdir'] = 'xsdir'

    # MDATA output
    if test.name in ['17', '20', '21', '22']:
        test.outputs['mdata'] = 'mdata'

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
