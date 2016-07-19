import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

names = ['abajez', 'abajezb', 'cone', 'conea', 'conelink', 'conelnk', 'cube01',
         'cube02', 'cube03', 'cube04', 'cube05', 'cube06a', 'cube06b', 'cube07',
         'cube08a', 'cube08b', 'cube09a', 'cube09b', 'cyl01', 'cyl02', 'cyl03',
         'cyl04', 'cyl04a', 'cyl04ar', 'cyl04b', 'cyl04br', 'cyl04c', 'cyl04d',
         'cyl04r', 'cyl05a', 'cyl05b', 'cyl05c', 'gdv_a', 'gdv_b', 'godiva',
         'hfm001', 'hfm001a', 'hfm001c', 'hfm015', 'hfm015a', 'hfm015b',
         'hfm015c', 'hfm015d', 'hfm015z', 'lat16', 'lat16a', 'lat16b',
         'pr_block01', 'pr_block01a', 'pr_block01b', 'zeus2', 'zeus2a',
         'zeus2b', 'zeus2bh', 'zeus2h']

def setup_test(name, args):
    test = dagtest.dagmc_test(name, args)

    test.physics = 'mcnp6'

    # Input file name format
    test.inputs['inp'] = test.name + '.i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # FATAL option
    if test.name in ['cyl04br']:
        test.flags.append('fatal')

    # I option
    if test.name in ['cube02', 'cube03', 'cube04']:
        test.flags.append('i')

    # IP option
    if test.name in ['lat16b']:
        test.flags.append('ip')

    # M option
    if test.name in ['abajez', 'cone', 'cyl01', 'cyl02', 'cyl03', 'cyl04',
                     'cyl04r', 'godiva', 'hfm001', 'hfm015', 'lat16',
                     'pr_block01', 'slug', 'zeus2', 'zeus2h']:
        test.flags.append('m')

    # Cross section data
    test.dirs['xsdir'] = '../../xsec_data'
    test.dirs['xslib'] = '../../xsec_data'
    if test.name in ['cube02', 'cube03', 'cube04', 'cube05', 'cube06b',
                     'cube07', 'cyl01', 'cyl02', 'cyl03', 'cyl04', 'cyl04r',
                     'cyl04b', 'cyl04c', 'cyl04d', 'cyl04br', 'cyl05b',
                     'cyl05c', 'lat16', 'lat16b', 'pr_block01', 'pr_block01a',
                     'pr_block01b']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'

    # Unstructured mesh files
    test.dirs['um'] = 'Files'
    if test.name in ['abajez', 'abajeza']:
        test.other['um'] = 'abajez.inp'

    # LINKOUT dependencies
    if test.name in ['abajezb']:
        test.depends.append(['abajez', 'linkout'])
    if test.name in ['conelink']:
        test.depends.append(['cone', 'linkout'])
    if test.name in ['cube02', 'cube03', 'cube04', 'cube05', 'cube06b',
                     'cube07', 'cube08b', 'cube09b']:
        test.depends.append(['cube01', 'linkout'])
    if test.name in ['cyl04b', 'cyl04c', 'cyl04d']:
        test.depends.append(['cyl04', 'linkout'])
    if test.name in ['cyl04br']:
        test.depends.append(['cyl04r', 'linkout'])
    if test.name in ['cyl05b']:
        test.depends.append(['cyl01', 'linkout'])
    if test.name in ['cyl05c']:
        test.depends.append(['cyl02', 'linkout'])
    if test.name in ['gdv_b']:
        test.depends.append(['godiva', 'linkout'])
    if test.name in ['hfm001c']:
        test.depends.append(['hfm001', 'linkout'])
    if test.name in ['hfm015b', 'hfm015c', 'hfm015d', 'hfm015z']:
        test.depends.append(['hfm015', 'linkout'])
    if test.name in ['lat16b']:
        test.depends.append(['lat16', 'linkout'])
    if test.name in ['pr_block01b']:
        test.depends.append(['pr_block01', 'linkout'])
    if test.name in ['slugb']:
        test.depends.append(['slug', 'linkout'])
    if test.name in ['zeus2b']:
        test.depends.append(['zeus2', 'linkout'])
    if test.name in ['zeus2bh']:
        test.depends.append(['zeus2h', 'linkout'])

    # MESHTAL output
    if test.name in ['pr_block01a', 'pr_block01b']:
        test.outputs['meshtal'] = 'meshtal'

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
