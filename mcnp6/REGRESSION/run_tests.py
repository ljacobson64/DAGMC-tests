import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27', '28', '29', '30',
         '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
         '41', '42', '43', '44', '45', '46', '47', '48', '49', '50',
         '51', '52', '53', '54', '55', '56', '57', '58', '59', '60',
         '61', '62', '63', '64', '65', '66', '67', '68', '69', '70',
         '71', '72', '73', '74', '75', '76', '77', '78', '79', '80',
         '81', '82', '83', '84', '85', '86', '87', '88', '89', '90',
         '91', '92', '93', '94', '95', '96', '97', '98', '99', '100',
         '101', '102', '103', '104', '105', '106', '107', '108', '109', '110',
         '111', '112', '113', '114', '115', '116', '117', '118', '119', '120',
         '121', '122', '123', '124', '125',               '128', '129', '130',
         '131', '132', '133',
         '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009',
         '1010', '1011', '1012', '1013', '1014', '1015', '1016']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = 'inp' + test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # "C 2" option
    if test.name in ['61']:
        test.flags.append('C 2')

    # CN option
    if test.name in ['25', '26', '104', '1002', '1009']:
        test.flags.append('CN')

    # FATAL option
    if test.name in ['01', '02', '07', '08', '09', '11', '12', '13', '14', '15',
                     '16', '17', '18', '19', '20', '21', '22', '23', '24', '25',
                     '26', '29', '30', '31', '33', '34', '38', '40', '67', '68',
                     '71', '76', '77', '89', '104', '123', '130', '133']:
        test.flags.append('fatal')

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.dirs['xslib'] = '../xsec_data'
    test.inputs['xsdir'] = 'testdir1'
    test.other['xslib'] = 'testlib1'

    # WWINP input
    test.dirs['wwinp'] = 'Files'
    if test.name in ['08', '10', '14', '93']:
        test.inputs['wwinp'] = 'wwinp' + test.name

    # COSY_MAP files
    test.dirs['cosy_map_1'] = 'Files'
    test.dirs['cosy_map_2'] = 'Files'
    test.dirs['cosy_map_3'] = 'Files'
    test.dirs['cosy_map_4'] = 'Files'
    test.dirs['cosy_map_5'] = 'Files'
    test.dirs['cosy_map_6'] = 'Files'
    if test.name in ['57']:
        test.other['cosy_map_1'] = '571'
        test.other['cosy_map_2'] = '572'
        test.other['cosy_map_3'] = '573'
        test.other['cosy_map_4'] = '574'
        test.other['cosy_map_5'] = '575'
        test.other['cosy_map_6'] = '576'

    # GENXS files
    test.dirs['genxs'] = 'Files'
    if test.name in ['63', '64', '73', '78', '79', '80', '81', '82', '91',
                     '106']:
        test.other['genxs'] = 'inxc'+ test.name

    # Unstructured mesh files
    test.dirs['um'] = 'Files'
    if test.name in ['1001', '1002', '1003', '1004', '1005', '1006', '1007',
                     '1008', '1009', '1010', '1011', '1012', '1013', '1014',
                     '1015', '1016']:
        test.other['um'] = 'um' + test.name + '.inp'

    # RSSA dependencies
    if test.name in ['08', '29']:
        test.depends.append(['07', 'rssa'])
    if test.name in ['22']:
        test.depends.append(['21', 'rssa'])
    if test.name in ['27']:
        test.depends.append(['09', 'rssa'])
    if test.name in ['34']:
        test.depends.append(['33', 'rssa'])

    # RUNTPE dependencies
    if test.name in ['25']:
        test.depends.append(['24', 'runtpe'])
    if test.name in ['26']:
        test.depends.append(['09', 'runtpe'])
    if test.name in ['61']:
        test.depends.append(['57', 'runtpe'])
    if test.name in ['104']:
        test.depends.append(['103', 'runtpe'])
    if test.name in ['1002']:
        test.depends.append(['1001', 'runtpe'])
    if test.name in ['1009']:
        test.depends.append(['1008', 'runtpe'])

    # SRCTP dependencies
    if test.name in ['17', '123']:
        test.depends.append(['009', 'srctp'])

    # WSSA dependencies
    if test.name in ['26']:
        test.depends.append(['09', 'rssa'])

    # MESHTAL output
    if test.name in ['39', '40', '53', '54', '55', '56', '57', '60', '61', '96',
                     '105', '111', '112', '118', '119', '120', '131', '132',
                     '1001', '1002', '1003', '1012', '1013', '1014']:
        test.outputs['meshtal'] = 'meshtal'

    # PTRAC output
    if test.name in ['01', '02', '08', '18', '23']:
        test.outputs['ptrac'] = 'ptrac'

    # WWONE output
    if test.name in ['10', '11', '12', '13', '100', '101']:
        test.outputs['wwone'] = 'wwone'

    # WWOUT output
    if test.name in ['08', '10', '12', '14']:
        test.outputs['wwout'] = 'wwout'

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
