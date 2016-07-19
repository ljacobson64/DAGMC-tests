import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['Au10600MeVperA_Cu', 'Au559MeVperA_Cu', 'bg4.5C_pi_Laq', 'C290C',
         'C800C_REP', 'Ca140MeVperA_Be', 'inp71corREP', 'inp75cor_bREP',
         'inpl05REP', 'Ne2.1GeVPb', 'Ne241U_REP', 'Ne393U_REP', 'Ne800Cu_REP',
         'p23000Te_Laq', 'p300000Ag_REP', 'p400GeVTa_GENXSREP', 'p800000Au_REP',
         'p800Au_CEM', 'p800Au_Laq', 'Pb1000LbREP', 'Pb32706000Cu',
         'Si600CuREP', 'Sn112_1AGeV_Sn112', 'Sn124_1AGeV_Sn124']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # GENXS files
    test.dirs['genxs'] = 'Files'
    if test.name in ['Au10600MeVperA_Cu', 'Ca140MeVperA_Be',
                     'Sn112_1AGeV_Sn112', 'Sn124_1AGeV_Sn124']:
        test.other['genxs'] = 'inxc69'
    if test.name in ['Au559MeVperA_Cu']:
        test.other['genxs'] = 'inxc68'
    if test.name in ['bg4.5C_pi_Laq']:
        test.other['genxs'] = 'inxs025'
    if test.name in ['Ne2.1GeVPb']:
        test.other['genxs'] = 'inxc88'
    if test.name in ['p23000Te_Laq', 'p800000Au_REP', 'p800Au_Laq']:
        test.other['genxs'] = 'inxc97'
    if test.name in ['p300000Ag_REP']:
        test.other['genxs'] = 'inxc98'
    if test.name in ['p400GeVTa_GENXSREP']:
        test.other['genxs'] = 'inxc38'
    if test.name in ['p800Au_CEM']:
        test.other['genxs'] = 'inxc96'
    if test.name in ['Pb32706000Cu']:
        test.other['genxs'] = 'inxc70'

    return test

def setup_tests(names, args):
    tests = []
    for name in names:
        tests.append(setup_test(name, args))
    return tests

args = dagtest.parse_args()

if __name__ != '__main__':
    args.tests = 'all'
if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = setup_tests(names_to_run, args)

if __name__ == '__main__':
    dagtest.run_multiple_tests(names_to_run, tests, args)
