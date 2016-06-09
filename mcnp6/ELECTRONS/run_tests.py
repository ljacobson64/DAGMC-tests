import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010',
         '011', '012', '013', '014', '015', '016', '017', '018', '019', '020',
         '021', '022', '023', '024', '025', '026', '027', '028', '029', '030',
         '031', '032', '033', '034', '035', '036', '037', '038', '039',
         '051', '052', '053', '054', '055', '056', '057', '058', '059',
         '061', '062', '063', '064', '065', '066', '067', '068', '069',
         '071', '072', '073', '074', '075', '076', '077', '078', '079',
                              '124', '125', '126', '127', '128', '129', '130',
         '131', '132', '133', '134', '135', '136', '137', '138', '139', '140',
         '141', '142', '143',
                       '153',
         '171', '172', '173', '174', '175', '176', '177']

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
    test.inputs['inp'] = 'inp' + test.name

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

    # FATAL option
    if test.name in ['001', '002', '003', '139']:
        test.flags.append('fatal')

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.dirs['xslib'] = '../xsec_data'
    if test.name in ['010', '011', '012', '013', '014', '015', '016', '017',
                     '018', '019', '020', '021', '022', '023', '024', '025',
                     '026', '027', '028', '029', '030', '031', '032', '033',
                     '034', '035', '036', '037', '038', '039', '041', '042',
                     '043', '044', '045', '046', '047', '048', '049', '051',
                     '052', '053', '054', '055', '056', '057', '058', '059',
                     '061', '062', '063', '064', '065', '066', '067', '068',
                     '069', '071', '072', '073', '074', '075', '076', '077',
                     '078', '079', '100', '153', '155', '156', '171', '172',
                     '173', '174', '175', '176', '177']:
        test.inputs['xsdir'] = 'xsdirph'
    if test.name in ['001', '002', '003', '004', '009', '139']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'

    # RSSA dependencies
    if test.name in ['004']:
        test.depends.append(['001', 'rssa'])

    # MESHTAL output
    if test.name in ['009']:
        test.outputs['meshtal'] = 'meshtal'

    # PTRAC output
    if test.name in ['003']:
        test.outputs['ptrac'] = 'ptrac'

    # WWOUT output
    if test.name in ['139']:
        test.outputs['wwout'] = 'wwout'

dagtest.run_multiple_tests(names_to_run, tests, args)