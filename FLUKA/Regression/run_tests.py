import inspect
import os
import sys

current_dir = \
    os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import fluka_testing as ft

args = ft.parse_args()

temp = [1, 2, 3, 11, 12, 13, 21, 22, 41, 42, 51, 52, 61, 62]
names = [''] * len(temp) * 2
for i, name in enumerate(temp):
    names[i] = str(name).zfill(2) + '_nat'
for i, name in enumerate(temp):
    names[i + len(temp)] = str(name).zfill(2) + '_dag'

if args.tests == 'all':
    names_to_run = names
else:
    names_to_run = args.tests

tests = {}
for name in names_to_run:
    tests[name] = ft.fluka_test(name, args)
    test = tests[name]

    # Run types
    if test.name.split('_')[1] == 'nat':
        test.geom_type = 'native'
    elif test.name.split('_')[1] == 'dag':
        test.geom_type = 'dagmc'
    if test.name.split('_')[0] in ['41', '42']:
        test.run_type = 'usrbdx'
    elif test.name.split('_')[0] in ['61', '62']:
        test.run_type = 'code'
    else:
        test.run_type = 'usrtrack'

    # Number of runs
    if test.name.split('_')[0] in ['01', '61', '62']:
        test.num_runs = 1
    else:
        test.num_runs = 5

    # Directories
    test.dirs['orig'] = current_dir
    test.dirs['input'] = 'Inputs'
    test.dirs['result'] = os.path.join('Results', test.name)
    test.dirs['temp'] = os.path.join('Templates', test.name)
    if test.geom_type == 'dagmc':
        test.dirs['gcad'] = 'Geom_h5m'

    # Inputs
    test.inputs['inp'] = test.name + '.inp'
    if test.geom_type == 'dagmc':
        test.inputs['gcad'] = 'geom_' + test.name + '.h5m'

    # Outputs
    if test.run_type != 'code':
        #for i in range(test.numruns):
        #    istr = str(i).zfill(3)
        #    test.outputs['out' + istr] = test.name + istr + '.out'
        test.outputs['sum'] = test.name + '_sum.lis'
        test.outputs['tab'] = test.name + '_tab.lis'

ft.run_multiple_tests(names_to_run, tests, args)
