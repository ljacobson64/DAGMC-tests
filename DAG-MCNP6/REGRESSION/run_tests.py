import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['inp01', 'inp02', 'inp03', 'inp04', 'inp05', 'inp06', 'inp07', 'inp08',
         'inp09', 'inp10', 'inp11', 'inp12', 'inp13', 'inp14', 'inp15', 'inp16',
         'inp17', 'inp18', 'inp19', 'inp20', 'inp21', 'inp22', 'inp23', 'inp24',
         'inp25', 'inp26', 'inp27', 'inp28', 'inp29', 'inp30', 'inp31', 'inp32',
         'inp33', 'inp34', 'inp35', 'inp36', 'inp37', 'inp38', 'inp39', 'inp40',
         'inp41', 'inp42', 'inp43', 'inp44', 'inp45', 'inp46', 'inp47', 'inp48',
         'inp49', 'inp50', 'inp51', 'inp52', 'inp53', 'inp54', 'inp55', 'inp56',
         'inp57', 'inp58', 'inp59', 'inp60', 'inp61', 'inp62', 'inp63', 'inp64',
         'inp65', 'inp66', 'inp67', 'inp68', 'inp69', 'inp70', 'inp71', 'inp72',
         'inp73', 'inp74', 'inp75', 'inp76', 'inp77', 'inp78', 'inp79', 'inp80',
         'inp81', 'inp82', 'inp83', 'inp84', 'inp85', 'inp86', 'inp87', 'inp88',
         'inp89', 'inp90', 'inp91', 'inp92', 'inp93', 'inp94', 'inp95', 'inp96',
         'inp97', 'inp98', 'inp99', 'inp100', 'inp101', 'inp102', 'inp103',
         'inp104', 'inp105', 'inp106', 'inp107', 'inp108', 'inp109', 'inp110',
         'inp111', 'inp112', 'inp113', 'inp114', 'inp115', 'inp116', 'inp117',
         'inp118', 'inp119', 'inp120', 'inp121', 'inp122', 'inp123', 'inp124',
         'inp125', 'inp128', 'inp129', 'inp130', 'inp131', 'inp132', 'inp133',
         'inp1001', 'inp1002', 'inp1003', 'inp1004', 'inp1005', 'inp1006',
         'inp1007', 'inp1008', 'inp1009', 'inp1010', 'inp1011', 'inp1012',
         'inp1013', 'inp1014', 'inp1015', 'inp1016']

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
