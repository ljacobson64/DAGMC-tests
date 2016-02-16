import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['BE08', 'C29', 'CCR20', 'COAIR', 'COTEF', 'FE09', 'FS1ONN', 'FS3OFN',
         'FS3ONP', 'FS7OFP', 'FS7ONN', 'H2O19', 'KERMIN', 'LI616', 'N31',
         'PB14', 'SKYINP', 'SMAIR', 'SMTEF']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp5'

    # Directories
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['log'] = 'Logs'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name

    # Common input
    test.inputs['inp'] = test.name + 'i'
    test.inputs['gcad'] = 'geom_' + test.name + '.h5m'
    test.other['sat'] = 'geom_' + test.name + '.sat'

    # Logs
    test.logs['gcad'] = 'geom_' + test.name + '.h5m.log'

    # Common output
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Special output
    if name in ['FS3OFN', 'FS3ONP', 'FS7OFP', 'FS7ONN']:
        test.outputs['wwout'] = 'wwout'

dagtest.run_multiple_tests(names_to_run, tests, args)
