import argparse
import os
from subprocess import call
import multiprocessing as mp

def run_mcnp2cad(inp_file):
    sat_file = os.path.join(os.path.dirname(os.path.dirname(inp_file)),
                            'Geom_sat', os.path.basename(inp_file) + '.sat')
    run_string = 'mcnp2cad ' + inp_file + ' -o ' + sat_file + ' --geomver 1902'
    print run_string
    call(run_string, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run mcnp2cad.')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    return args

args = parse_args()
jobs = args.jobs

# Find all the files in directories called "Inputs_orig"
inp_dirs = []
inp_files = []
for root, dirnames, filenames in os.walk('.'):
    if os.path.basename(root) == 'Inputs_orig':
        inp_dirs.append(root)
        for f in filenames:
            inp_files.append(os.path.join(root, f))

# Create the "Geom_sat" directories where the .sat files will be placed
for inp_dir in inp_dirs:
    sat_dir = os.path.join(os.path.dirname(inp_dir), 'Geom_sat')
    if not os.path.exists(sat_dir):
        os.makedirs(sat_dir)

if jobs > 1:
    pool = mp.Pool(processes = jobs)

for inp_file in inp_files:
    if jobs > 1:
        pool.apply_async(run_mcnp2cad, args = (inp_file,))
    else:
        run_mcnp2cad(inp_file)

if jobs > 1:
    pool.close()
    pool.join()
