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
         'PB14', 'SKYINP', 'SMAIR', 'SMTEF',
         'duct_therm_neutron_oneleg_conc', 'duct_therm_neutron_oneleg_reinf',
         'duct_therm_neutron_threeleg_conc',
         'duct_therm_neutron_threeleg_reinf', 'duct_therm_neutron_twoleg_conc',
         'duct_therm_neutron_twoleg_reinf', 'fns_config1_neutron_onaxis',
         'fns_config3_neutron_offaxis', 'fns_config3_photon_onaxis',
         'fns_config7_neutron_onaxis', 'fns_config7_photon_offaxis', 'lps_berl',
         'lps_carbon', 'lps_conc', 'lps_iron', 'lps_lead', 'lps_lith',
         'lps_nitro', 'lps_pu239', 'lps_u235', 'lps_u238', 'lps_water',
         'photon_kerma', 'photon_skyshine']

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
    if name[0].isupper():
        test.inputs['inp'] = test.name + 'i'
    else:
        test.inputs['inp'] = test.name + '.inp'

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

dagtest.run_multiple_tests(names_to_run, tests, args)
