import os
import sys
from subprocess import call

inp_files = sys.argv[1:]

os.makedirs('orig')

for inp_file in inp_files:
    call('cp ' + inp_file + ' ' + 'orig', shell = True)
    reader = open(inp_file, 'r')
    lines = reader.readlines()
    reader.close()

    writer = open(inp_file, 'w')
    writer.write(lines[0])
    num_blank_lines = 0
    for line in lines[1:]:
        if num_blank_lines < 2:
            writer.write('c ' + line)
        elif line.strip().lower().startswith('imp'):
            writer.write('c ' + line)
        else:
            writer.write(line)
        if line.strip() == '':
            num_blank_lines += 1
    writer.close()
