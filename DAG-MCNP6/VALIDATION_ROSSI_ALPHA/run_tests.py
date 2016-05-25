import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['heu-met-fast-001', 'heu-met-fast-028', 'heu-met-fast-072-case-1',
         'heu-met-fast-073', 'heu-met-inter-006-case-1',
         'heu-met-inter-006-case-4', 'ieu-met-fast-007-case-4',
         'ieu-sol-therm-004-case-46', 'ieu-sol-therm-007-case-30',
         'pu-met-fast-001', 'pu-met-fast-006', 'pu-met-fast-008-case-2',
         'u233-met-fast-001', 'u233-met-fast-006']

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
    test.dirs['input'] = 'Inputs'
    test.dirs['sat'] = 'Geom_sat'
    test.dirs['gcad'] = 'Geom_h5m'
    test.dirs['result'] = 'Results/' + test.name
    test.dirs['temp'] = 'Templates/' + test.name
    test.inputs['gcad'] = test.inputs['inp'] + '.h5m'
    test.other['sat'] = test.inputs['inp'] + '.sat'
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.dirs['xsdir'] = 'Files'
    test.inputs['xsdir'] = 'xsdir_endf71'

dagtest.run_multiple_tests(names_to_run, tests, args)
