import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['heu_point', 'Pu239ACE', 'Pu239CINDER', 'U233ACE', 'U233CINDER',
         'U235ACE', 'U235CINDER']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name

    # Common
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs_dagmc'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name
    test.inputs['gcad'] = test.inputs['inp'] + '.h5m'
    test.other['sat'] = test.inputs['inp'] + '.sat'
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Tally card files
    test.dirs['tally_cards'] = 'Files'
    if test.name in ['heu_point']:
        test.other['tally_cards'] = 'tally_u_dagmc.dat'

dagtest.run_multiple_tests(names_to_run, tests, args)
