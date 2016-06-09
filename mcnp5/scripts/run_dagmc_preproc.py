import argparse
import os
from subprocess import call
import multiprocessing as mp

def run_dagmc_preproc(sat_file):
    h5m_file = os.path.join(os.path.dirname(os.path.dirname(sat_file)),
                            'Geom_h5m', os.path.basename(sat_file)[:-4] + '.h5m')
    run_string = 'dagmc_preproc ' + sat_file + ' -o ' + h5m_file
    print run_string
    call(run_string, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run dagmc_preproc.')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    return args

args = parse_args()
jobs = args.jobs

# Find all the files in directories called "Geom_sat"
sat_dirs = []
sat_files = []
for root, dirnames, filenames in os.walk('.'):
    if os.path.basename(root) == 'Geom_sat':
        sat_dirs.append(root)
        for f in filenames:
            sat_files.append(os.path.join(root, f))

# Create the "Geom_h5m" directories where the .h5m files will be placed
for sat_dir in sat_dirs:
    h5m_dir = os.path.join(os.path.dirname(sat_dir), 'Geom_h5m')
    if not os.path.exists(h5m_dir):
        os.makedirs(h5m_dir)

if jobs > 1:
    pool = mp.Pool(processes = jobs)

for sat_file in sat_files:
    if jobs > 1:
        pool.apply_async(run_dagmc_preproc, args = (sat_file,))
    else:
        run_dagmc_preproc(sat_file)

if jobs > 1:
    pool.close()
    pool.join()
