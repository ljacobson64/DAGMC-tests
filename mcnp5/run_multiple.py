import imp
import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
base_dir = os.path.dirname(current_dir)
sys.path.insert(0, base_dir)
import dagmc_testing as dagtest

suites = ['DAGMC',
          'Meshtally'
          'Regression',
          'VALIDATION_CRITICALITY',
          'VALIDATION_SHIELDING',
          'VERIFICATION_KEFF']

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
