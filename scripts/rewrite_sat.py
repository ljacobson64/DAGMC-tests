import sys
from subprocess import call

satfiles = sys.argv

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
