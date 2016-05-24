import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['Au10600MeVperA_Cu', 'Au559MeVperA_Cu', 'bg4.5C_pi_Laq', 'C290C',
         'C800C_REP', 'Ca140MeVperA_Be', 'inp71corREP', 'inp75cor_bREP',
         'inpl05REP', 'Ne2.1GeVPb', 'Ne241U_REP', 'Ne393U_REP', 'Ne800Cu_REP',
         'p23000Te_Laq', 'p300000Ag_REP', 'p400GeVTa_GENXSREP', 'p800000Au_REP',
         'p800Au_CEM', 'p800Au_Laq', 'Pb1000LbREP', 'Pb32706000Cu',
         'Si600CuREP', 'Sn112_1AGeV_Sn112', 'Sn124_1AGeV_Sn124']

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
