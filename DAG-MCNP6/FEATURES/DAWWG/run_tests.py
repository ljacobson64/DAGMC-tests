import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['abajezb', 'abajez', 'conea', 'cone', 'conenk', 'conelnk', 'cube01',
         'cube02', 'cube03', 'cube04', 'cube05', 'cube06a', 'cube06b', 'cube07',
         'cube08a', 'cube08b', 'cube09a', 'cube09b', 'cyl01', 'cyl02', 'cyl03',
         'cyl04a', 'cyl04ar', 'cyl04b', 'cyl04br', 'cyl04c', 'cyl04d', 'cyl04',
         'cyl04r', 'cyl05a', 'cyl05b', 'cyl05c', 'gdv_a', 'gdv_b', 'gova',
         'hfm001a', 'hfm001c', 'hfm001', 'hfm015a', 'hfm015b', 'hfm015c',
         'hfm015d', 'hfm015', 'hfm015z', 'lat16a', 'lat16b', 'lat16',
         'pr_block01a', 'pr_block01b', 'pr_block01', 'zeus2a', 'zeus2bh',
         'zeus2b', 'zeus2h', 'zeus2']

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
    test.inputs['inp'] = test.name + '.i'

    # Common
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name
    test.inputs['gcad'] = test.inputs['inp'] + '.h5m'
    test.other['sat'] = test.inputs['inp'] + '.sat'
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

dagtest.run_multiple_tests(names_to_run, tests, args)
