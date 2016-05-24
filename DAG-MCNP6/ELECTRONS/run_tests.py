import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['inp001', 'inp002', 'inp003', 'inp004', 'inp005', 'inp006', 'inp007',
         'inp008', 'inp009', 'inp010', 'inp011', 'inp012', 'inp013', 'inp014',
         'inp015', 'inp016', 'inp017', 'inp018', 'inp019', 'inp020', 'inp021',
         'inp022', 'inp023', 'inp024', 'inp025', 'inp026', 'inp027', 'inp028',
         'inp029', 'inp030', 'inp031', 'inp032', 'inp033', 'inp034', 'inp035',
         'inp036', 'inp037', 'inp038', 'inp039', 'inp051', 'inp052', 'inp053',
         'inp054', 'inp055', 'inp056', 'inp057', 'inp058', 'inp059', 'inp061',
         'inp062', 'inp063', 'inp064', 'inp065', 'inp066', 'inp067', 'inp068',
         'inp069', 'inp071', 'inp072', 'inp073', 'inp074', 'inp075', 'inp076',
         'inp077', 'inp078', 'inp079', 'inp124', 'inp125', 'inp126', 'inp127',
         'inp128', 'inp129', 'inp130', 'inp131', 'inp132', 'inp133', 'inp134',
         'inp135', 'inp136', 'inp137', 'inp138', 'inp139', 'inp140', 'inp141',
         'inp142', 'inp143', 'inp153', 'inp171', 'inp172', 'inp173', 'inp174',
         'inp175', 'inp176', 'inp177']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp6'

    # Directories
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name

    # Common input
    test.inputs['inp'] = test.name
    test.inputs['gcad'] = test.name + '.h5m'
    test.other['sat'] = test.name + '.sat'

    # Common output
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

dagtest.run_multiple_tests(names_to_run, tests, args)
