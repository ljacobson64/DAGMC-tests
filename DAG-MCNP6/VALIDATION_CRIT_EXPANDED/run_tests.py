import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['heu-comp-inter-003-case-6', 'heu-met-fast-001',
         'heu-met-fast-003-case-10', 'heu-met-fast-003-case-11',
         'heu-met-fast-003-case-12', 'heu-met-fast-003-case-1',
         'heu-met-fast-003-case-2', 'heu-met-fast-003-case-3',
         'heu-met-fast-003-case-4', 'heu-met-fast-003-case-5',
         'heu-met-fast-003-case-6', 'heu-met-fast-003-case-7',
         'heu-met-fast-003-case-8', 'heu-met-fast-003-case-9',
         'heu-met-fast-004-case-1', 'heu-met-fast-008',
         'heu-met-fast-009-case-1', 'heu-met-fast-009-case-2',
         'heu-met-fast-011', 'heu-met-fast-012', 'heu-met-fast-013',
         'heu-met-fast-014', 'heu-met-fast-015', 'heu-met-fast-018-case-2',
         'heu-met-fast-019-case-2', 'heu-met-fast-020-case-2',
         'heu-met-fast-021-case-2', 'heu-met-fast-022-case-2',
         'heu-met-fast-026-case-c-11', 'heu-met-fast-028',
         'heu-met-inter-006-case-1', 'heu-met-inter-006-case-2',
         'heu-met-inter-006-case-3', 'heu-met-inter-006-case-4',
         'heu-sol-therm-013-case-1', 'heu-sol-therm-013-case-2',
         'heu-sol-therm-013-case-3', 'heu-sol-therm-013-case-4',
         'heu-sol-therm-032', 'ieu-comp-therm-002-case-3',
         'ieu-met-fast-001-case-1', 'ieu-met-fast-001-case-2',
         'ieu-met-fast-001-case-3', 'ieu-met-fast-001-case-4',
         'ieu-met-fast-002', 'ieu-met-fast-003-case-2',
         'ieu-met-fast-004-case-2', 'ieu-met-fast-005-case-2',
         'ieu-met-fast-006-case-2', 'ieu-met-fast-007-case-4',
         'leu-comp-therm-008-case-11', 'leu-comp-therm-008-case-1',
         'leu-comp-therm-008-case-2', 'leu-comp-therm-008-case-5',
         'leu-comp-therm-008-case-7', 'leu-comp-therm-008-case-8',
         'leu-sol-therm-002-case-1', 'leu-sol-therm-002-case-2',
         'leu-sol-therm-007-case-14', 'leu-sol-therm-007-case-30',
         'leu-sol-therm-007-case-32', 'leu-sol-therm-007-case-36',
         'leu-sol-therm-007-case-49', 'mix-comp-therm-002-case-pnl30',
         'mix-comp-therm-002-case-pnl31', 'mix-comp-therm-002-case-pnl32',
         'mix-comp-therm-002-case-pnl33', 'mix-comp-therm-002-case-pnl34',
         'mix-comp-therm-002-case-pnl35', 'mix-met-fast-001',
         'mix-met-fast-003', 'mix-met-fast-008-case-7', 'pu-comp-inter-001',
         'pu-met-fast-001', 'pu-met-fast-002', 'pu-met-fast-003-case-103',
         'pu-met-fast-005', 'pu-met-fast-006', 'pu-met-fast-008-case-2',
         'pu-met-fast-009', 'pu-met-fast-010', 'pu-met-fast-011',
         'pu-met-fast-018', 'pu-met-fast-019', 'pu-met-fast-020',
         'pu-met-fast-021-case-1', 'pu-met-fast-021-case-2',
         'pu-met-fast-022-case-2', 'pu-met-fast-023-case-2',
         'pu-met-fast-024-case-2', 'pu-met-fast-025-case-2',
         'pu-met-fast-026-case-2', 'pu-sol-therm-009-case-3a',
         'pu-sol-therm-011-case-16-5', 'pu-sol-therm-011-case-18-1',
         'pu-sol-therm-011-case-18-6', 'pu-sol-therm-018-case-9',
         'pu-sol-therm-021-case-1', 'pu-sol-therm-021-case-3',
         'pu-sol-therm-034-case-1', 'u233-comp-therm-001-case-3',
         'u233-comp-therm-001-case-6', 'u233-met-fast-001',
         'u233-met-fast-002-case-1', 'u233-met-fast-002-case-2',
         'u233-met-fast-003-case-1', 'u233-met-fast-003-case-2',
         'u233-met-fast-004-case-1', 'u233-met-fast-004-case-2',
         'u233-met-fast-005-case-1', 'u233-met-fast-005-case-2',
         'u233-met-fast-006', 'u233-sol-inter-001-case-1',
         'u233-sol-therm-001-case-1', 'u233-sol-therm-001-case-2',
         'u233-sol-therm-001-case-3', 'u233-sol-therm-001-case-4',
         'u233-sol-therm-001-case-5', 'u233-sol-therm-008']

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

    # Cross section data
    test.dirs['xsdir'] = 'Files'
    test.inputs['xsdir'] = 'xsdir_endf71'

dagtest.run_multiple_tests(names_to_run, tests, args)
