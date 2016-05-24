import commands
import os
from subprocess import call

# Find all the files in the "Inputs_orig" directory
inp_files = commands.getstatusoutput('find Inputs_orig -type f')[1].split()

if not os.path.exists('Inputs'):
    os.makedirs('Inputs')

for inp_orig in inp_files:
    reader = open(inp_orig, 'r')
    lines_in = reader.readlines()
    reader.close()

    # Put the DAG-MCNP input file in the "Inputs" directory
    inp_file = os.path.join('Inputs', os.path.basename(inp_orig))

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
