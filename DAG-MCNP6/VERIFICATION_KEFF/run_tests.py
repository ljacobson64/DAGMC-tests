import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

args = dagtest.parse_args()

names = ['prob01i', 'prob02i', 'prob03i', 'prob04i', 'prob05i', 'prob06i',
         'prob07i', 'prob08i', 'prob09i', 'prob10i', 'prob11i', 'prob12i',
         'prob13i', 'prob14i', 'prob15i', 'prob16i', 'prob17i', 'prob18i',
         'prob19i', 'prob20i', 'prob21i', 'prob22i', 'prob23i', 'prob24i',
         'prob25i', 'prob26i', 'prob27i', 'prob28i', 'prob29i', 'prob30i',
         'prob31i', 'prob32i', 'prob33i', 'prob34i', 'prob35i', 'prob36i',
         'prob37i', 'prob38i', 'prob39i', 'prob40i', 'prob41i', 'prob42i',
         'prob43i', 'prob44i', 'prob45i', 'prob46i', 'prob47i', 'prob48i',
         'prob49i', 'prob50i', 'prob51i', 'prob52i', 'prob53i', 'prob54i',
         'prob55i', 'prob56i', 'prob57i', 'prob58i', 'prob59i', 'prob60i',
         'prob61i', 'prob62i', 'prob63i', 'prob64i', 'prob65i', 'prob66i',
         'prob67i', 'prob68i', 'prob69i', 'prob70i', 'prob71i', 'prob72i',
         'prob73i', 'prob74i', 'prob75i']

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = dagtest.dagmc_test(name, args)
    test = tests[name]

    test.physics = 'mcnp6'

    # Common
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
    test.dirs['xsdir'] = 'Inputs'
    test.inputs['xsdir'] = 'keffdir1'
    test.other['xslib'] = 'kefflib1'

dagtest.run_multiple_tests(names_to_run, tests, args)
