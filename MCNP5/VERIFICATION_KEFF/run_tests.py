import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = range(1, 76);
for i, name in enumerate(names):
    names[i] = str(name).zfill(2)

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

    # xsdir setup
    test.dirs['xsdir'] = '../xsec_data'
    test.inputs['xsdir'] = 'keffdir1'
    test.other['xslib'] = 'kefflib1'

    # Common input
    test.inputs['inp'] = 'prob' + test.name + 'i'
    test.inputs['gcad'] = 'geom_' + test.name + '.h5m'
    test.other['sat'] = 'geom_' + test.name + '.sat'

    # Logs
    test.logs['gcad'] = 'geom_' + test.name + '.h5m.log'

    # Common output
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Special output
    if name in ['09', '10', '23']:
        test.outputs['ptrac'] = 'ptrac'

dagtest.run_multiple_tests(names_to_run, tests, args)
