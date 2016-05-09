import argparse
import commands
import os
import sys
from subprocess import call
import multiprocessing as mp

def run_dagmc_preproc(sat_file):
    dirname = os.path.dirname(os.path.dirname(sat_file))
    name = os.path.basename(sat_file)[:-4]
    h5m_file = os.path.join(dirname, 'Geom_h5m', name + '.h5m')
    if not os.path.exists(os.path.join(dirname, 'Geom_h5m')):
        os.makedirs(os.path.join(dirname, 'Geom_h5m'))
    call('dagmc_preproc ' + sat_file + ' -o ' + h5m_file, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run dagmc_preproc.')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    return args

args = parse_args()
jobs = args.jobs

sat_files = commands.getstatusoutput('find . -type f -name *.sat')[1].split()

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
