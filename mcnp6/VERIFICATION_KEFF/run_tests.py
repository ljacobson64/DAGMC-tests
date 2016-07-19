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
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
         '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
         '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
         '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
         '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
         '71', '72', '73', '74', '75']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = 'prob' + test.name + 'i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = 'Files'
    test.dirs['xslib'] = 'Files'
    test.inputs['xsdir'] = 'keffdir1'
    test.other['xslib'] = 'kefflib1'

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
