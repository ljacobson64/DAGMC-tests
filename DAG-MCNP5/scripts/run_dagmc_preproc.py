import argparse
import os
import sys
from subprocess import call
import multiprocessing as mp

def run_dagmc_preproc(inp_file):
    dirname = os.path.dirname(inp_file)
    name = os.path.basename(inp_file)[:-4]
    sat_file = inp_file
    h5m_file = dirname + '/' + name + '.h5m'
    call('dagmc_preproc ' + sat_file + ' -o ' + h5m_file, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run dagmc_preproc.')
    parser.add_argument('files', nargs = '*',
                        help = 'files on which to run dagmc_preproc')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    return args

args = parse_args()
inp_files = args.files
jobs = args.jobs

if jobs > 1:
    pool = mp.Pool(processes = jobs)

for inp_file in inp_files:
    if jobs > 1:
        pool.apply_async(run_dagmc_preproc, args = (inp_file,))
    else:
        run_dagmc_preproc(inp_file)

if jobs > 1:
    pool.close()
    pool.join()
