import sys
from subprocess import call

inpfiles = sys.argv

for inpfile in inpfiles:
    satfile = "geom" + inpfile[3:] + ".sat"
    call("mcnp2cad " + inpfile + " -o " + satfile, shell = True)
