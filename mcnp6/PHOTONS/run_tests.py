import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['001',               '004',        '006',               '009', '010',
         '011', '012', '013', '014', '015', '016', '017', '018', '019', '020',
         '021', '022', '023', '024', '025', '026', '027', '028', '029', '030',
         '031', '032', '033', '034', '035', '036', '037', '038', '039', '040',
                '042', '043', '044', '045',
         '051', '052', '053', '054', '055', '056', '057', '058', '059',
                '062', '063', '064', '065', '066', '067', '068', '069', '070',
         '071', '072', '073', '074', '075', '076']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = 'inp' + test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.inputs['xsdir'] = 'xsdirph'

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
