import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['av01', 'av01_noRR', 'av02', 'av03', 'av03_noRR', 'av04', 'av05',
         'av05_noRR', 'av06', 'av07', 'av08', 'av08_noRR', 'av09', 'av10',
         'av11_noRR', 'av12', 'av12_noRR', 'av13', 'av13_noRR', 'av14',
         'av14_noRR', 'av17', 'av17_noRR', 'av18', 'av18_noRR', 'av19', 'av20',
         'av20_noRR', 'av21', 'av21_noRR', 'av22', 'av22_noRR', 'av23',
         'av23_noRR', 'cy01', 'cy02', 'cy03', 'cy04', 'cy04_noRR', 'cy05',
         'cy06', 'cy06_noRR', 'cy07', 'cy07_noRR', 'cy08', 'cy09', 'cy10',
         'cy10_noRR', 'cy11', 'cy12', 'cy12_noRR', 'cy13', 'cy13_noRR', 'cy14',
         'cy14_noRR', 'cy15', 'cy15_noRR', 'cy16', 'cy16_noRR', 'cy17', 'cy18',
         'cy18_noRR', 'cy19', 'cy19_noRR', 'cy20', 'cy20_noRR', 'cy21',
         'cy21_noRR', 'cy22', 'cy22_noRR', 'cy23', 'cy23_noRR', 'cy24', 'cy25',
         'cy26', 'cy27', 'cy28', 'cy28_noRR', 'cy29', 'cy30', 'cy31', 'cy32',
         'cy33', 'cy33_noRR', 'cy34', 'cy35', 'cy36', 'cy36_noRR', 'cy37',
         'cy38', 'cy38_noRR', 'cy39', 'cy39_noRR', 'df01', 'df02', 'df03',
         'lat01', 'line01', 'line02', 'line03', 'line04', 'line05', 'line06',
         'line07', 'rg01', 'rg02', 'rg03', 'rg03_noRR', 'rg04', 'rg04_noRR',
         'rg05', 'rg05_noRR', 'rg06', 'rg06_noRR', 'rg07', 'rg07_noRR', 'rg08',
         'rg09', 'rg10', 'rg11', 'rg11_noRR', 'rg12', 'rg12_noRR', 'x01a',
         'x01v', 'x01v_noRR', 'x01w', 'x02a', 'x02b', 'x02i', 'x02i_noRR',
         'x02v', 'x02v_noRR', 'x02w_noRR', 'x03a', 'x03i', 'x03i_noRR', 'x03v',
         'x03v_noRR', 'x03w', 'x03w_noRR', 'x04a', 'x04b', 'x04e', 'x04e_noRR',
         'x04w', 'x04w_noRR', 'x05a', 'x05e', 'x05e_noRR', 'x05w', 'x05w_noRR',
         'x11a', 'x11v', 'x11v_noRR', 'x11w', 'x12a', 'x12b', 'x12i',
         'x12i_noRR', 'x12v', 'x12v_noRR', 'x12w', 'x13a', 'x13i', 'x13i_noRR',
         'x13v', 'x13v_noRR', 'x13w', 'x13w_noRR', 'x14a', 'x14b', 'x14e',
         'x14e_noRR', 'x14w', 'x14w_noRR', 'x15a', 'x15e', 'x15e_noRR', 'x15w',
         'x15w_noRR', 'x21a', 'x21v', 'x21v_noRR', 'x21w', 'x22a', 'x22b',
         'x22v', 'x22v_noRR', 'x22w', 'x23a', 'x23v', 'x23v_noRR', 'x23w',
         'x23w_noRR', 'x24a', 'x24b', 'x24w', 'x24w_noRR', 'x25a', 'x25e',
         'x25e_noRR', 'x25w', 'x25w_noRR', 'x31a', 'x31p', 'x31w', 'x81h',
         'x81h_noRR']

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
    test.inputs['inp'] = 'inp_' + test.name

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

    # FATAL option
    if test.name in ['rg03', 'rg03_noRR', 'rg11', 'rg11_noRR', 'x25w', 'x25e',
                     'x25e_noRR', 'x25w_noRR']:
        test.flags.append('fatal')

    # WWINP input
    test.dirs['wwinp'] = 'Files'
    if test.name in ['cy02', 'cy04', 'cy05', 'cy12', 'cy13', 'cy14', 'cy18',
                     'cy19', 'cy23', 'cy33', 'cy36', 'cy38', 'cy39',
                     'cy04_noRR', 'cy12_noRR', 'cy13_noRR', 'cy14_noRR',
                     'cy18_noRR', 'cy19_noRR', 'cy23_noRR', 'cy33_noRR',
                     'cy36_noRR', 'cy38_noRR', 'cy39_noRR']:
        test.inputs['wwinp'] = 'phtww'
    if test.name in ['x04w', 'x04w_noRR', 'x04e', 'x04e_noRR']:
        test.inputs['wwinp'] = 'wwinp4'
    if test.name in ['x05w', 'x05w_noRR', 'x05e', 'x05e_noRR']:
        test.inputs['wwinp'] = 'wwinp5'
    if test.name in ['x14w', 'x14w_noRR', 'x14e', 'x14e_noRR']:
        test.inputs['wwinp'] = 'wwinp14'
    if test.name in ['x15w', 'x15w_noRR', 'x15e', 'x15e_noRR']:
        test.inputs['wwinp'] = 'wwinp15'
    if test.name in ['x24w', 'x24w_noRR']:
        test.inputs['wwinp'] = 'wwinp24'
    if test.name in ['x25w', 'x25e', 'x25e_noRR', 'x25w_noRR']:
        test.inputs['wwinp'] = 'wwinp25'

dagtest.run_multiple_tests(names_to_run, tests, args)
