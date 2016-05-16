import sys
from subprocess import call

inp_files = sys.argv[1:]

for inp_file in inp_files:
    orig_inp_file = "orig_" + inp_file
    call("mv " + inp_file + " " + orig_inp_file, shell = True)
    reader = open(orig_inp_file, 'r')
    lines = reader.readlines()
    reader.close()

    writer = open(inp_file, 'w')
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
