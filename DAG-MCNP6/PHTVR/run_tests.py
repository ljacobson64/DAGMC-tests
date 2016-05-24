import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['inp_av01', 'inp_av01_noRR', 'inp_av02', 'inp_av03', 'inp_av03_noRR',
         'inp_av04', 'inp_av05', 'inp_av05_noRR', 'inp_av06', 'inp_av07',
         'inp_av08', 'inp_av08_noRR', 'inp_av09', 'inp_av10', 'inp_av11_noRR',
         'inp_av12', 'inp_av12_noRR', 'inp_av13', 'inp_av13_noRR', 'inp_av14',
         'inp_av14_noRR', 'inp_av17', 'inp_av17_noRR', 'inp_av18',
         'inp_av18_noRR', 'inp_av19', 'inp_av20', 'inp_av20_noRR', 'inp_av21',
         'inp_av21_noRR', 'inp_av22', 'inp_av22_noRR', 'inp_av23',
         'inp_av23_noRR', 'inp_cy01', 'inp_cy02', 'inp_cy03', 'inp_cy04',
         'inp_cy04_noRR', 'inp_cy05', 'inp_cy06', 'inp_cy06_noRR', 'inp_cy07',
         'inp_cy07_noRR', 'inp_cy08', 'inp_cy09', 'inp_cy10', 'inp_cy10_noRR',
         'inp_cy11', 'inp_cy12', 'inp_cy12_noRR', 'inp_cy13', 'inp_cy13_noRR',
         'inp_cy14', 'inp_cy14_noRR', 'inp_cy15', 'inp_cy15_noRR', 'inp_cy16',
         'inp_cy16_noRR', 'inp_cy17', 'inp_cy18', 'inp_cy18_noRR', 'inp_cy19',
         'inp_cy19_noRR', 'inp_cy20', 'inp_cy20_noRR', 'inp_cy21',
         'inp_cy21_noRR', 'inp_cy22', 'inp_cy22_noRR', 'inp_cy23',
         'inp_cy23_noRR', 'inp_cy24', 'inp_cy25', 'inp_cy26', 'inp_cy27',
         'inp_cy28', 'inp_cy28_noRR', 'inp_cy29', 'inp_cy30', 'inp_cy31',
         'inp_cy32', 'inp_cy33', 'inp_cy33_noRR', 'inp_cy34', 'inp_cy35',
         'inp_cy36', 'inp_cy36_noRR', 'inp_cy37', 'inp_cy38', 'inp_cy38_noRR',
         'inp_cy39', 'inp_cy39_noRR', 'inp_df01', 'inp_df02', 'inp_df03',
         'inp_lat01', 'inp_line01', 'inp_line02', 'inp_line03', 'inp_line04',
         'inp_line05', 'inp_line06', 'inp_line07', 'inp_rg01', 'inp_rg02',
         'inp_rg03', 'inp_rg03_noRR', 'inp_rg04', 'inp_rg04_noRR', 'inp_rg05',
         'inp_rg05_noRR', 'inp_rg06', 'inp_rg06_noRR', 'inp_rg07',
         'inp_rg07_noRR', 'inp_rg08', 'inp_rg09', 'inp_rg10', 'inp_rg11',
         'inp_rg11_noRR', 'inp_rg12', 'inp_rg12_noRR', 'inp_x01a', 'inp_x01v',
         'inp_x01v_noRR', 'inp_x01w', 'inp_x02a', 'inp_x02b', 'inp_x02i',
         'inp_x02i_noRR', 'inp_x02v', 'inp_x02v_noRR', 'inp_x02w_noRR',
         'inp_x03a', 'inp_x03i', 'inp_x03i_noRR', 'inp_x03v', 'inp_x03v_noRR',
         'inp_x03w', 'inp_x03w_noRR', 'inp_x04a', 'inp_x04b', 'inp_x04e',
         'inp_x04e_noRR', 'inp_x04w', 'inp_x04w_noRR', 'inp_x05a', 'inp_x05e',
         'inp_x05e_noRR', 'inp_x05w', 'inp_x05w_noRR', 'inp_x11a', 'inp_x11v',
         'inp_x11v_noRR', 'inp_x11w', 'inp_x12a', 'inp_x12b', 'inp_x12i',
         'inp_x12i_noRR', 'inp_x12v', 'inp_x12v_noRR', 'inp_x12w', 'inp_x13a',
         'inp_x13i', 'inp_x13i_noRR', 'inp_x13v', 'inp_x13v_noRR', 'inp_x13w',
         'inp_x13w_noRR', 'inp_x14a', 'inp_x14b', 'inp_x14e', 'inp_x14e_noRR',
         'inp_x14w', 'inp_x14w_noRR', 'inp_x15a', 'inp_x15e', 'inp_x15e_noRR',
         'inp_x15w', 'inp_x15w_noRR', 'inp_x21a', 'inp_x21v', 'inp_x21v_noRR',
         'inp_x21w', 'inp_x22a', 'inp_x22b', 'inp_x22v', 'inp_x22v_noRR',
         'inp_x22w', 'inp_x23a', 'inp_x23v', 'inp_x23v_noRR', 'inp_x23w',
         'inp_x23w_noRR', 'inp_x24a', 'inp_x24b', 'inp_x24w', 'inp_x24w_noRR',
         'inp_x25a', 'inp_x25e', 'inp_x25e_noRR', 'inp_x25w', 'inp_x25w_noRR',
         'inp_x31a', 'inp_x31p', 'inp_x31w', 'inp_x81h', 'inp_x81h_noRR']

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
