import argparse
import os
import sys
from subprocess import call
import multiprocessing as mp

def run_mcnp2cad(inp_file):
    sat_file = os.path.dirname(inp_file) + '/geom_' + os.path.basename(inp_file) + '.sat'
    call('mcnp2cad ' + inp_file + ' -o ' + sat_file, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run mcnp2cad.')
    parser.add_argument('files', nargs = '*',
                        help = 'files on which to run mcnp2cad')
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
        pool.apply_async(run_mcnp2cad, args = (inp_file,))
    else:
        run_mcnp2cad(inp_file)

if jobs > 1:
    pool.close()
    pool.join()
