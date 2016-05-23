import argparse
import commands
import os
from subprocess import call
import multiprocessing as mp

def run_mcnp2cad(inp_file):
    sat_file = os.path.join('Geom_sat', os.path.basename(inp_file) + '.sat')
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

# Find all the files in the "Inputs" directory
inp_files = commands.getstatusoutput('find Inputs_orig -type f')[1].split()

if not os.path.exists('Geom_sat'):
    os.makedirs('Geom_sat')

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
