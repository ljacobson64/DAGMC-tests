from subprocess import call
import os

inpfiles = []

for fname in os.listdir("."):
    if fname.startswith("inp"):
        inpfiles.append(fname)

for inpfile in inpfiles:
    satfile = "geom" + inpfile[3:] + ".sat"
    call("mcnp2cad " + inpfile + " -o " + satfile, shell = True)
