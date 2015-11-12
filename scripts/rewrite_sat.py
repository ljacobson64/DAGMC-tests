from subprocess import call
import os

satfiles = []

for fname in os.listdir("."):
    if fname.endswith(".sat"):
        satfiles.append(fname)

for satfile in satfiles:
    orig_satfile = "orig_" + satfile
    call("mv " + satfile + " " + orig_satfile, shell = True)
    writer = open("rewrite_" + satfile + ".jou",'w')
    writer.write("import acis \"" + orig_satfile + "\"\n")
    writer.write("set attribute on\n")
    writer.write("set geometry version 1902\n")
    writer.write("export acis \"" + satfile + "\" overwrite\n")
    writer.close()
    call("cubit -batch -nographics -nojournal rewrite_" + satfile + ".jou &", shell = True)
