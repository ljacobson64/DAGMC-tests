import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['inp001', 'inp004', 'inp006', 'inp009', 'inp010', 'inp011', 'inp012',
         'inp013', 'inp014', 'inp015', 'inp016', 'inp017', 'inp018', 'inp019',
         'inp020', 'inp021', 'inp022', 'inp023', 'inp024', 'inp025', 'inp026',
         'inp027', 'inp028', 'inp029', 'inp030', 'inp031', 'inp032', 'inp033',
         'inp034', 'inp035', 'inp036', 'inp037', 'inp038', 'inp039', 'inp040',
         'inp042', 'inp043', 'inp044', 'inp045', 'inp051', 'inp052', 'inp053',
         'inp054', 'inp055', 'inp056', 'inp057', 'inp058', 'inp059', 'inp062',
         'inp063', 'inp064', 'inp065', 'inp066', 'inp067', 'inp068', 'inp069',
         'inp070', 'inp071', 'inp072', 'inp073', 'inp074', 'inp075', 'inp076']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp6'

    # Common
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name
    test.inputs['inp'] = test.name
    test.inputs['gcad'] = test.name + '.h5m'
    test.other['sat'] = test.name + '.sat'
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.inputs['xsdir'] = 'xsdirph'

dagtest.run_multiple_tests(names_to_run, tests, args)
