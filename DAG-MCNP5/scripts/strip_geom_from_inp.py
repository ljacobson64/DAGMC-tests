import os

def strip_geom_from_inp(inp_orig_file):
    reader = open(inp_orig_file, 'r')
    lines_in = reader.readlines()
    reader.close()

    # Put the DAG-MCNP input file in the "Inputs" directory
    inp_file = os.path.join(os.path.dirname(os.path.dirname(inp_orig_file)),
                            'Inputs', os.path.basename(inp_orig_file))

    num_blank_lines = 0
    prdmp_found = False
    lines_out = []

    # Write the title card
    lines_out.append(lines_in[0])

    # Loop over all the lines in the original input file
    for line in lines_in[1:]:
        line = line.rstrip()

        # Blank line found
        if line.strip() == '':
            num_blank_lines += 1
            # MCNP does not read lines after the third blank line
            if num_blank_lines >= 3:
                break
            lines_out.append('c\n')

        # Comment out cell and surface cards
        elif num_blank_lines < 2:
            lines_out.append('c ' + line + '\n')

        # Comment out importance card if it's found in the data card block
        elif line.strip().lower().startswith('imp'):
            lines_out.append('c ' + line + '\n')

        # Make sure the third entry on the PRDMP card is -2
        elif line.strip().lower().startswith('prdmp'):
            prdmp_found = True
            prdmp_in = line.split()
            prdmp_out = ['prdmp', 'j', 'j', '-2', '', '']
            if prdmp_in[1].lower() == '2j':
                j2 = 1
                prdmp_out[1] = prdmp_in[1]
                prdmp_out[2] = ''
            else:
                j2 = 0
                prdmp_out[1] = prdmp_in[1]
                prdmp_out[2] = prdmp_in[2]
            if len(prdmp_in) > 4 - j2:
                prdmp_out[4] = prdmp_in[4 - j2]
            if len(prdmp_in) > 5 - j2:
                prdmp_out[5] = prdmp_in[5 - j2]
            prdmp_out = ' '.join([x for x in prdmp_out if x])
            lines_out.append(prdmp_out + '\n')

        # Write line as normal
        else:
            lines_out.append(line + '\n')

    # Write the PRDMP card if it wasn't already written
    if not prdmp_found:
        lines_out.append('prdmp 2j -2\n')

    writer = open(inp_file, 'wb')

    # File is likely a real MCNP input file
    if num_blank_lines in [2, 3]:
        for line in lines_out:
            writer.write(line)

    # File is likely not a real MCNP input file
    else:
        for line in lines_in:
            writer.write(line)

    writer.close()

# Find all the files in directories called "Inputs_orig"
inp_orig_dirs = []
inp_orig_files = []
for root, dirnames, filenames in os.walk('.'):
    if os.path.basename(root) == 'Inputs_orig':
        inp_orig_dirs.append(root)
        for f in filenames:
            inp_orig_files.append(os.path.join(root, f))

# Create the "Inputs" directories where the new input files will be placed
for inp_orig_dir in inp_orig_dirs:
    inp_dir = os.path.join(os.path.dirname(inp_orig_dir), 'Inputs')
    if not os.path.exists(inp_dir):
        os.makedirs(inp_dir)

for inp_orig_file in inp_orig_files:
    strip_geom_from_inp(inp_orig_file)
