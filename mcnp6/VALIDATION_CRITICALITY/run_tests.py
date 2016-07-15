import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['BAWXI2', 'BIGTEN', 'FLAT23', 'FLAT25', 'FLATPU', 'FLSTF1', 'GODIVA',
         'GODIVR', 'HISHPG', 'ICT2C3', 'IMF03', 'IMF04', 'JEZ233', 'JEZ240',
         'JEZPU', 'LST2C2', 'ORNL10', 'ORNL11', 'PNL2', 'PNL33', 'PUBTNS',
         'PUSH2O', 'SB25', 'SB5RN3', 'STACY36', 'THOR', 'TT2C11', 'UH3C6',
         'UMF5C2', 'ZEBR8H', 'ZEUS2']

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
    test.inputs['inp'] = test.name + 'i'

    # Common
    test.dirs['orig'] = current_dir
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = 'Files'
    test.inputs['xsdir'] = 'xsdir_endf71'

dagtest.run_multiple_tests(names_to_run, tests, args)
