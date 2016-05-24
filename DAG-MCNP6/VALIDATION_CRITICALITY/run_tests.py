import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['BAWXI2i', 'BIGTENi', 'FLAT23i', 'FLAT25i', 'FLATPUi', 'FLSTF1i',
         'GODIVAi', 'GODIVRi', 'HISHPGi', 'ICT2C3i', 'IMF03i', 'IMF04i',
         'JEZ233i', 'JEZ240i', 'JEZPUi', 'LST2C2i', 'ORNL10i', 'ORNL11i',
         'PNL2i', 'PNL33i', 'PUBTNSi', 'PUSH2Oi', 'SB25i', 'SB5RN3i',
         'STACY36i', 'THORi', 'TT2C11i', 'UH3C6i', 'UMF5C2i', 'ZEBR8Hi',
         'ZEUS2i']

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
    test.inputs['inp'] = test.name
    test.inputs['gcad'] = test.name + '.h5m'
    test.other['sat'] = test.name + '.sat'
    test.outputs['outp'] = 'outp'
    test.outputs['mctal'] = 'mctal'

    # Cross section data
    test.inputs['xsdir'] = 'xsdir_endf71'

dagtest.run_multiple_tests(names_to_run, tests, args)
