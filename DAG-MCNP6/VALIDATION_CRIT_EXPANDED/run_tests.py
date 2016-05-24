import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['heu-comp-inter-003-case-6.i', 'heu-met-fast-001.i',
         'heu-met-fast-003-case-10.i', 'heu-met-fast-003-case-11.i',
         'heu-met-fast-003-case-12.i', 'heu-met-fast-003-case-1.i',
         'heu-met-fast-003-case-2.i', 'heu-met-fast-003-case-3.i',
         'heu-met-fast-003-case-4.i', 'heu-met-fast-003-case-5.i',
         'heu-met-fast-003-case-6.i', 'heu-met-fast-003-case-7.i',
         'heu-met-fast-003-case-8.i', 'heu-met-fast-003-case-9.i',
         'heu-met-fast-004-case-1.i', 'heu-met-fast-008.i',
         'heu-met-fast-009-case-1.i', 'heu-met-fast-009-case-2.i',
         'heu-met-fast-011.i', 'heu-met-fast-012.i', 'heu-met-fast-013.i',
         'heu-met-fast-014.i', 'heu-met-fast-015.i',
         'heu-met-fast-018-case-2.i', 'heu-met-fast-019-case-2.i',
         'heu-met-fast-020-case-2.i', 'heu-met-fast-021-case-2.i',
         'heu-met-fast-022-case-2.i', 'heu-met-fast-026-case-c-11.i',
         'heu-met-fast-028.i', 'heu-met-inter-006-case-1.i',
         'heu-met-inter-006-case-2.i', 'heu-met-inter-006-case-3.i',
         'heu-met-inter-006-case-4.i', 'heu-sol-therm-013-case-1.i',
         'heu-sol-therm-013-case-2.i', 'heu-sol-therm-013-case-3.i',
         'heu-sol-therm-013-case-4.i', 'heu-sol-therm-032.i',
         'ieu-comp-therm-002-case-3.i', 'ieu-met-fast-001-case-1.i',
         'ieu-met-fast-001-case-2.i', 'ieu-met-fast-001-case-3.i',
         'ieu-met-fast-001-case-4.i', 'ieu-met-fast-002.i',
         'ieu-met-fast-003-case-2.i', 'ieu-met-fast-004-case-2.i',
         'ieu-met-fast-005-case-2.i', 'ieu-met-fast-006-case-2.i',
         'ieu-met-fast-007-case-4.i', 'leu-comp-therm-008-case-11.i',
         'leu-comp-therm-008-case-1.i', 'leu-comp-therm-008-case-2.i',
         'leu-comp-therm-008-case-5.i', 'leu-comp-therm-008-case-7.i',
         'leu-comp-therm-008-case-8.i', 'leu-sol-therm-002-case-1.i',
         'leu-sol-therm-002-case-2.i', 'leu-sol-therm-007-case-14.i',
         'leu-sol-therm-007-case-30.i', 'leu-sol-therm-007-case-32.i',
         'leu-sol-therm-007-case-36.i', 'leu-sol-therm-007-case-49.i',
         'mix-comp-therm-002-case-pnl30.i', 'mix-comp-therm-002-case-pnl31.i',
         'mix-comp-therm-002-case-pnl32.i', 'mix-comp-therm-002-case-pnl33.i',
         'mix-comp-therm-002-case-pnl34.i', 'mix-comp-therm-002-case-pnl35.i',
         'mix-met-fast-001.i', 'mix-met-fast-003.i',
         'mix-met-fast-008-case-7.i', 'pu-comp-inter-001.i',
         'pu-met-fast-001.i', 'pu-met-fast-002.i', 'pu-met-fast-003-case-103.i',
         'pu-met-fast-005.i', 'pu-met-fast-006.i', 'pu-met-fast-008-case-2.i',
         'pu-met-fast-009.i', 'pu-met-fast-010.i', 'pu-met-fast-011.i',
         'pu-met-fast-018.i', 'pu-met-fast-019.i', 'pu-met-fast-020.i',
         'pu-met-fast-021-case-1.i', 'pu-met-fast-021-case-2.i',
         'pu-met-fast-022-case-2.i', 'pu-met-fast-023-case-2.i',
         'pu-met-fast-024-case-2.i', 'pu-met-fast-025-case-2.i',
         'pu-met-fast-026-case-2.i', 'pu-sol-therm-009-case-3a.i',
         'pu-sol-therm-011-case-16-5.i', 'pu-sol-therm-011-case-18-1.i',
         'pu-sol-therm-011-case-18-6.i', 'pu-sol-therm-018-case-9.i',
         'pu-sol-therm-021-case-1.i', 'pu-sol-therm-021-case-3.i',
         'pu-sol-therm-034-case-1.i', 'u233-comp-therm-001-case-3.i',
         'u233-comp-therm-001-case-6.i', 'u233-met-fast-001.i',
         'u233-met-fast-002-case-1.i', 'u233-met-fast-002-case-2.i',
         'u233-met-fast-003-case-1.i', 'u233-met-fast-003-case-2.i',
         'u233-met-fast-004-case-1.i', 'u233-met-fast-004-case-2.i',
         'u233-met-fast-005-case-1.i', 'u233-met-fast-005-case-2.i',
         'u233-met-fast-006.i', 'u233-sol-inter-001-case-1.i',
         'u233-sol-therm-001-case-1.i', 'u233-sol-therm-001-case-2.i',
         'u233-sol-therm-001-case-3.i', 'u233-sol-therm-001-case-4.i',
         'u233-sol-therm-001-case-5.i', 'u233-sol-therm-008.i']

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
