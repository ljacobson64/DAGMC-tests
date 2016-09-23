import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names =['01', '02', '03', '04',       '06', '07', '08', '09', '10',
              '12',                                     '19', '20', 
        '21', '22', '23',             '26', '27', '28', '29', '30', 
        '31', '32', '33', '34', '35', '36', '37',       '39', 
        '41', '42',                         '47', 
        '61', '62', '63', '64', '65', '66', '67', '68', 
                                      '86',                   '90', 
                    '93', '94', '95',             '98', '99']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp5'

    # Input file name format
    test.inputs['inp'] = 'inp' + test.name

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # CN option
    if test.name == '26':
        test.flags.append('CN')

    # FATAL option
    if test.name in ['01', '02', '07', '11', '12', '18', '19', '20', '21',
                     '22', '23', '26', '30', '77', '89']:
        test.flags.append('fatal')

    # I option
    if test.name in ['62']:
        test.flags.append('i')

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.dirs['xslib'] = '../xsec_data'
    test.inputs['xsdir'] = 'testdir1'
    test.other['xslib'] = 'testlib1'

    # LCAD input
    test.dirs['lcad'] = 'Files'
    if test.name in ['62']:
        test.inputs['lcad'] = 'lcad' + test.name

    # WWINP input
    test.dirs['wwinp'] = 'Files'
    if test.name in ['08', '10', '93']:
        test.inputs['wwinp'] = 'wwinp' + test.name

    # RSSA dependencies
    if test.name in ['08', '29']:
        test.depends.append(['07', 'rssa'])
    if test.name in ['22']:
        test.depends.append(['21', 'rssa'])
    if test.name in ['27']:
        test.depends.append(['09', 'rssa'])
    if test.name in ['34']:
        test.depends.append(['33', 'rssa'])
    if test.name in ['26']:
        test.depends.append(['09', 'wssa'])

    # RUNTPE dependencies
    if test.name in ['26']:
        test.depends.append(['09', 'runtpe'])

    # MESHTAL output
    if test.name in ['39']:
        test.outputs['meshtal'] = 'meshtal'

    # PTRAC output
    if test.name in ['02', '03', '08', '23']:
        test.outputs['ptrac'] = 'ptrac'

    # WWONE output
    if test.name in ['08', '12']:
        test.outputs['wwone'] = 'wwone'

    # WWOUT output
    if test.name in ['08', '10', '12']:
        test.outputs['wwout'] = 'wwout'

    # No MCTAL output
    if test.name in ['62']:
        del test.outputs['mctal']

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
