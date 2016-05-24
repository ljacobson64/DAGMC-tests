import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['BE08i', 'C29i', 'CCR20i', 'COAIRi', 'COTEFi', 'FE09i', 'FS1ONNi',
         'FS3OFNi', 'FS3ONPi', 'FS7OFPi', 'FS7ONNi', 'H2O19i', 'KERMINi',
         'LI616i', 'N31i', 'PB14i', 'SKYINPi', 'SMAIRi', 'SMTEFi',
         'duct_therm_neutron_oneleg_conc.inp',
         'duct_therm_neutron_oneleg_reinf.inp',
         'duct_therm_neutron_threeleg_conc.inp',
         'duct_therm_neutron_threeleg_reinf.inp',
         'duct_therm_neutron_twoleg_conc.inp',
         'duct_therm_neutron_twoleg_reinf.inp',
         'fns_config1_neutron_onaxis.inp', 'fns_config3_neutron_offaxis.inp',
         'fns_config3_photon_onaxis.inp', 'fns_config7_neutron_onaxis.inp',
         'fns_config7_photon_offaxis.inp', 'lps_berl.inp', 'lps_carbon.inp',
         'lps_conc.inp', 'lps_iron.inp', 'lps_lead.inp', 'lps_lith.inp',
         'lps_nitro.inp', 'lps_pu239.inp', 'lps_u235.inp', 'lps_u238.inp',
         'lps_water.inp', 'photon_kerma.inp', 'photon_skyshine.inp']

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

dagtest.run_multiple_tests(names_to_run, tests, args)
