import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['bg4.5C_pi_CEM', 'bg4.5GeV_Nb_30CEM_0', 'bg4.5GeV_Nb_30CEM',
         'cu800b-cor', 'cu800c-cor', 'cu800i-cor', 'fe1200', 'g300cu', 'inp01a',
         'inp01', 'inpc05', 'inppfe', 'inp_pTi100', 'n1000Bi_CEM', 'n175fe',
         'n542Bi_GENXS', 'n542BiREP', 'p160Au_He4_GENXS', 'p160Au_He4_REP',
         'p18-H2O-TTY_C', 'p18-H2O-TTY', 'p35MeVLi7Bert', 'p35MeVLi7CEM',
         'p35MeVLi7lib4', 'p392Bi_GENXS', 'p392Pb_GENXS', 'p63Pb_GENXS_1',
         'p63Pb_n_cemREP', 'p730c_pi', 'p800Tb_Berto', 'p800Tb_CEMo',
         'p800Tb_INCLo', 'p800Th_Bert', 'p800Th_CEM', 'p800Th_INCL',
         'pip1500Fe_n']

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

    # Other files
    if test.name in ['inp01']:
        test.other['genxs'] = 'inxc01'
    if test.name in ['inpc05']:
        test.other['genxs'] = 'inxc05'
    if test.name in ['p63Pb_GENXS_1']:
        test.other['genxs'] = 'inxc06'
    if test.name in ['p160Au_He4_GENXS']:
        test.other['genxs'] = 'inxc07'
    if test.name in ['n542Bi_GENXS']:
        test.other['genxs'] = 'inxc08'
    if test.name in ['p392Bi_GENXS', 'p392Pb_GENXS']:
        test.other['genxs'] = 'inxc18'
    if test.name in ['inp01a']:
        test.other['genxs'] = 'inxc79'
    if test.name in ['p800Tb_Berto', 'p800Tb_CEMo', 'p800Tb_INCLo',
                     'p800Th_Bert', 'p800Th_CEM', 'p800Th_INCL']:
        test.other['genxs'] = 'inxc95'
    if test.name in ['g300cu']:
        test.other['genxs'] = 'inxcg1'
    if test.name in ['pip1500Fe_n']:
        test.other['genxs'] = 'inxcp1'
    if test.name in ['inppfe']:
        test.other['genxs'] = 'inxcpfe'
    if test.name in ['inp_pTi100']:
        test.other['genxs'] = 'inxct9'
    if test.name in ['bg4.5GeV_Nb_30CEM_0']:
        test.other['genxs'] = 'inxs021'
    if test.name in ['bg4.5GeV_Nb_30CEM']:
        test.other['genxs'] = 'inxs022'
    if test.name in ['bg4.5C_pi_CEM']:
        test.other['genxs'] = 'inxs026'
    if test.name in ['n1000Bi_CEM']:
        test.other['genxs'] = 'inxs96'
    if test.name in ['p730c_pi']:
        test.other['genxs'] = 'xpc12s'
    
dagtest.run_multiple_tests(names_to_run, tests, args)
