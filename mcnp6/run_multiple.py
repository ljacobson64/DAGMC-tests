import imp
import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(current_dir)
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

suites = ['DELAYED_PARTICLES',
          'ELECTRONS',
          'KOBAYASHI',
          'MAG_FIELDS',
          'MCNPX_65',
          'MUONS',
          'PHOTONS',
          'PHTVR',
          'REGRESSION',
          'VALIDATION_CEM',
          'VALIDATION_CRIT_EXPANDED',
          'VALIDATION_CRITICALITY',
          'VALIDATION_LAQGSM',
          'VALIDATION_ROSSI_ALPHA',
          'VALIDATION_SHIELDING',
          'VERIFICATION_KEFF',
          'FEATURES/DAWWG',
          'FEATURES/FMESH_INC',
          'FEATURES/MODEL_DEV',
          'FEATURES/POINT_DETECTORS',
          'FEATURES/UNC',
#         'MCNPX_EXTENDED/avr',
#         'MCNPX_EXTENDED/class',
#         'MCNPX_EXTENDED/classgeom',
#         'MCNPX_EXTENDED/classvar',
#         'MCNPX_EXTENDED/heavyions',
#         'MCNPX_EXTENDED/mbody',
#         'MCNPX_EXTENDED/phys',
#         'MCNPX_EXTENDED/push',
#         'MCNPX_EXTENDED/test27a',
#         'MCNPX_EXTENDED/test27b',
#         'MCNPX_EXTENDED/test27c',
#         'MCNPX_EXTENDED/test27d',
#         'MCNPX_EXTENDED/test27e',
#         'MCNPX_EXTENDED/testburn',
#         'MCNPX_EXTENDED/testdndg',
#         'MCNPX_EXTENDED/testincl',
#         'MCNPX_EXTENDED/testmcnp',
#         'MCNPX_EXTENDED/testmesh',
#         'MCNPX_EXTENDED/testmix',
#         'MCNPX_EXTENDED/testxnew',
#         'MCNPX_EXTENDED/testxold',
#         'MCNPX_EXTENDED/zrecoil',
          ]

args = dagtest.parse_args(True)

if args.suites == 'all':
    suites_to_run = suites
else:
    suites_to_run = args.suites

# Loop over all the suites
names_to_run = []
tests_to_run = []
for suite in suites_to_run:
    # Add the location of the suite's run_tests.py to the path
    sys.path.insert(0, os.path.join(current_dir, suite))

    # Get the test information from the suite's run_tests.py
    f, pathname, desc = imp.find_module('run_tests')
    module = imp.load_module(suite, f, pathname, desc)
    f.close()
    for test in module.tests:
        names_to_run.append(test.name)
        tests_to_run.append(test)

    # Remove the location of the suite's run_tests.py from the path
    for i, d in enumerate(sys.path):
        if suite in d:
            sys.path.pop(i)
            break

if __name__ == '__main__':
    dagtest.run_multiple_tests(names_to_run, tests_to_run, args)
