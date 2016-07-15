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
         '031', '032', '033', '034', '035', '036', '037', '038', '039', '040',
         '041', '042', '043',
                '102', '103', '104', '105', '106', '107', '108', '109', '110',
         '111', '112', '113', '114', '115', '116', '117', '118', '119', '120',
         '121', '122', '123',                                    '129',
                                                                        '150',
         '201', '202', '203', '204', '205', '206', '207', '208', '209',
                                     '215', '216',
                                                                        '250',
         '301', '302', '303', '304', '305', '306',               '309',
                                                                 '329']

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
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # CN option
    if test.name in ['025', '026']:
        test.flags.append('CN')

    # FATAL option
    if test.name in ['001', '002', '008', '009', '011', '012', '014', '017',
                     '018', '017', '020', '022', '023', '025', '026', '029',
                     '034', '117', '123', '150']:
        test.flags.append('fatal')

    # Cross section data
    test.dirs['xsdir'] = '../xsec_data'
    test.dirs['xslib'] = '../xsec_data'
    if test.name in ['003', '004', '005', '006', '007', '013', '015', '016',
                     '019', '021', '024', '030', '031', '032', '033', '035',
                     '036', '037', '038', '040', '041', '042', '043', '102',
                     '103', '104', '105', '106', '107', '108', '109', '110',
                     '118', '119', '120', '121', '122', '129', '303', '304',
                     '306', '309', '329', '205', '206', '208', '209', '250']:
        test.inputs['xsdir'] = 'testdir1'
        test.other['xslib'] = 'testlib1'
    if test.name in ['123']:
        test.dirs['xsdir'] = '../xsec_data'
        test.inputs['xsdir'] = 'xsdir27d'

    # WWINP input
    test.dirs['wwinp'] = 'Files'
    if test.name in ['008', '010', '014']:
        test.inputs['wwinp'] = 'wwinp' + test.name
    if test.name in ['301']:
        test.inputs['wwinp'] = 'wwinp010'

    # GENXS files
    test.dirs['genxs'] = 'Files'
    if test.name in ['115', '116', '215', '216']:
        test.other['genxs'] = 'inxs' + test.name

    # RSSA dependencies
    if test.name in ['008', '029']:
        test.depends.append(['007', 'rssa'])
    if test.name in ['022']:
        test.depends.append(['021', 'rssa'])
    if test.name in ['027']:
        test.depends.append(['009', 'rssa'])
    if test.name in ['034']:
        test.depends.append(['033', 'rssa'])

    # RUNTPE dependencies
    if test.name in ['025']:
        test.depends.append(['024', 'runtpe'])
    if test.name in ['026']:
        test.depends.append(['009', 'runtpe'])

    # SRCTP dependencies
    if test.name in ['017']:
        test.depends.append(['009', 'srctp'])

    # WSSA dependencies
    if test.name in ['026']:
        test.depends.append(['009', 'rssa'])

    # MDATA output
    if test.name in ['039', '201', '202', '203', '204', '207', '302']:
        test.outputs['mdata'] = 'mdata'

    # PTRAC output
    if test.name in ['001', '002', '008', '018', '023', '117']:
        test.outputs['ptrac'] = 'ptrac'

    # WWOUT output
    if test.name in ['008', '010', '012', '014', '301']:
        test.outputs['wwout'] = 'wwout'

dagtest.run_multiple_tests(names_to_run, tests, args)
