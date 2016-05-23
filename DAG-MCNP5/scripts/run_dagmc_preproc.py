import argparse
import commands
import os
from subprocess import call
import multiprocessing as mp

def run_dagmc_preproc(sat_file):
    h5m_file = os.path.join('Geom_h5m', os.path.basename(sat_file)[:-4] + '.h5m')
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

# Find all the .sat files in the "Geom_sat" directory
sat_files = commands.getstatusoutput('find Geom_sat -type f -name *.sat')[1].split()

if not os.path.exists('Geom_h5m'):
    os.makedirs('Geom_h5m')

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
