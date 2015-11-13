import sys

inpfiles = sys.argv

for inpfile in inpfiles:
    orig_inpfile = "orig_" + inpfile
    call("mv " + inpfile + " " + orig_inpfile, shell = True)
    reader = open(orig_inpfile, 'r')
    lines = reader.readlines()
    reader.close()

    writer = open(inpfile, 'w')
    writer.write(lines[0])
    num_blank_lines = 0
    for line in lines[1:]:
        if num_blank_lines < 2:
            writer.write("c " + line)
        else:
            writer.write(line)
        if line.strip() == "":
            num_blank_lines += 1
    writer.close()
