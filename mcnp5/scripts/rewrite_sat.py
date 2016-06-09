import argparse
import sys
from subprocess import call
import multiprocessing as mp

def rewrite_sat(sat_file):
    orig_sat_file = "orig_" + sat_file
    call("mv " + sat_file + " " + orig_sat_file, shell = True)
    #sat_file = sat_file[:-5] + sat_file[-4:]
    writer = open("rewrite_" + sat_file + ".jou",'w')
    writer.write("import acis \"" + orig_sat_file + "\"\n")
    writer.write("set attribute on\n")
    writer.write("set geometry version 1902\n")
    writer.write("export acis \"" + sat_file + "\" overwrite\n")
    writer.close()
    call("cubit -batch -nographics -nojournal rewrite_" + sat_file + ".jou &", shell = True)

def parse_args():
    parser = argparse.ArgumentParser(description = "Run mcnp2cad.")
    parser.add_argument("files", nargs = "*",
                        help = "files on which to run mcnp2cad")
    parser.add_argument("-j", "--jobs", type = int, default = 1,
                        help = "number of jobs")
    args = parser.parse_args()
    return args

args = parse_args()
sat_files = args.files
jobs = args.jobs

if jobs > 1:
    pool = mp.Pool(processes = jobs)

for sat_file in sat_files:
    if jobs > 1:
        pool.apply_async(rewrite_sat, args = (sat_file,))
    else:
        rewrite_sat(sat_file)

if jobs > 1:
    pool.close()
    pool.join()
