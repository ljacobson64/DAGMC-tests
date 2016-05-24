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
         'inp036', 'inp037', 'inp038', 'inp039', 'inp040', 'inp041', 'inp042',
         'inp043', 'inp102', 'inp103', 'inp104', 'inp105', 'inp106', 'inp107',
         'inp108', 'inp109', 'inp110', 'inp111', 'inp112', 'inp113', 'inp114',
         'inp115', 'inp116', 'inp117', 'inp118', 'inp119', 'inp120', 'inp121',
         'inp122', 'inp123', 'inp129', 'inp150', 'inp201', 'inp202', 'inp203',
         'inp204', 'inp205', 'inp206', 'inp207', 'inp208', 'inp209', 'inp215',
         'inp216', 'inp250', 'inp301', 'inp302', 'inp303', 'inp304', 'inp305',
         'inp306', 'inp309', 'inp329']

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
