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
         'inp17', 'inp18', 'inp19', 'inp20', 'inp21', 'inp22']

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

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    if test.name in ['inp01', 'inp02', 'inp03', 'inp04', 'inp05', 'inp06',
                     'inp07', 'inp08', 'inp09', 'inp10', 'inp11', 'inp12']:
        test.inputs['xsdir'] = 'xsdirph'
    if test.name in ['inp13', 'inp19']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'
    if test.name in ['inp14', 'inp15', 'inp16', 'inp17', 'inp18', 'inp20',
                     'inp21', 'inp22']:
        test.inputs['xsdir'] = 'xsdir'

    # MDATA output
    if test.name in ['inp17', 'inp20', 'inp21', 'inp22']:
        test.outputs['mdata'] = 'mdata'

    # FATAL option
    if test.name in ['inp17']:
        test.flags.append('fatal')

dagtest.run_multiple_tests(names_to_run, tests, args)
