import argparse
import commands
import os
import sys
from subprocess import call
import multiprocessing as mp

def run_mcnp2cad(inp_file):
    dirname = os.path.dirname(os.path.dirname(inp_file))
    name = os.path.basename(inp_file)
    sat_file = os.path.join(dirname, 'Geom_sat', name + '.sat')
    if not os.path.exists(os.path.join(dirname, 'Geom_sat')):
        os.makedirs(os.path.join(dirname, 'Geom_sat'))
    call('mcnp2cad ' + inp_file + ' -o ' + sat_file, shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = 'Run mcnp2cad.')
    parser.add_argument('-j', '--jobs', type = int, default = 1,
                        help = 'number of jobs')
    args = parser.parse_args()
    return args

args = parse_args()
jobs = args.jobs

inp_files = commands.getstatusoutput('find . -type f')[1].split()

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
