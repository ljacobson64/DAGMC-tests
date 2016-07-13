import os

def read_data_cards(lines_in):
    num_lines = len(lines_in)

    # Loop over all the lines in the original input file
    num_blank_lines = 0
    num_lines_skip = 0
    i = -1
    while i < num_lines - 1:
        i += 1 + num_lines_skip
        num_lines_skip = 0
        line = lines_in[i]

        # Blank line
        if line.strip() == '':
            num_blank_lines += 1
            # MCNP does not read lines after the third blank line
            if num_blank_lines >= 3:
                break
            continue

        # Comment line
        elif line.split()[0].lower() == 'c':
            continue

        # Not data card
        if num_blank_lines != 2:
            continue

        # Data card
        # Figure out how many lines the data card spans
        lines_data = [line]
        j = i + 1
        while j < num_lines:
            line_data = lines_in[j]
            if not line_data:
                break
            if (line_data.startswith('     ') or
                line_data.split()[0].lower() == 'c'):
                lines_data.append(line_data)
                j += 1
            else:
                break
        for line_data in reversed(lines_data):
            if line_data.split()[0] == 'c':
                lines_data.pop()
            else:
                break
        num_lines_skip = len(lines_data) - 1

        # Figure out whether the data card is an IMP card and if it is, load
        # the importance data into memory
        tokens = []
        imps = []
        for line_data in lines_data:
            for token in line_data.split():
                tokens.append(token)
        if 'imp:' in tokens[0]:
            for token in tokens[1:]:
                if token[-1] == 'r':
                    num_repeat = int(token[:-1])
                    for j in range(num_repeat):
                        imps.append(imps[-1])
                elif token[-1] == 'i':
                    num_interp_lin = int(token[:-1])
                elif token[-1] == 'ilog':
                    num_interp_log = int(token[:-4])
                elif token[-1] == 'm':
                    mult = float(token[-1])
                    imps.append(imps[-1] * mult)
                else:
                    imps.append(float(token))
            break

    return imps

def strip_imp0_from_inp(inp_orig_file):
    # Read input from file
    reader = open(inp_orig_file, 'r')
    lines_in = reader.readlines()
    reader.close()

    # Strip trailing whitespace
    for i, line in enumerate(lines_in):
        lines_in[i] = line.rstrip()
    num_lines = len(lines_in)

    # Read the data cards
    imps = read_data_cards(lines_in)

    # Put the mcnp2cad input file in the "Inputs_mcnp2cad" directory
    inp_file = os.path.join(os.path.dirname(os.path.dirname(inp_orig_file)),
                            'Inputs_mcnp2cad', os.path.basename(inp_orig_file))

    # Loop over all the lines in the original input file
    lines_out = []
    num_blank_lines = 0
    num_lines_skip = 0
    cell_index = -1
    i = -1
    while i < num_lines - 1:
        i += 1 + num_lines_skip
        num_lines_skip = 0
        line = lines_in[i]

        # Title card
        if i == 0:
            lines_out.append(line + '\n')

        # Blank line
        elif line.strip() == '':
            num_blank_lines += 1
            # MCNP does not read lines after the third blank line
            if num_blank_lines >= 3:
                break
            lines_out.append('\n')

        # Comment line
        elif line.split()[0].lower() == 'c':
            lines_out.append(line + '\n')

        # Cell card
        elif num_blank_lines == 0:
            cell_index += 1
            
            # Figure out how many lines the cell definition spans
            lines_cell = [line]
            j = i + 1
            while j < num_lines:
                line_cell = lines_in[j]
                if not line_cell:
                    break
                if (line_cell.startswith('     ') or
                    line_cell.split()[0].lower() == 'c'):
                    lines_cell.append(line_cell)
                    j += 1
                else:
                    break
            num_lines_skip = len(lines_cell) - 1

            # Get the cell's importance
            if imps:  # specified in data cards
                imp_found = True
                imp = imps[cell_index]
            else:  # specified with cell card
                tokens = []
                imp = -1
                imp_found = False
                for line_cell in lines_cell:
                    for token in line_cell.split():
                        tokens.append(token)
                for k, token in enumerate(tokens):
                    if token.lower().startswith('imp:'):
                        imp_found = True
                        if '=' in token:
                            imp = float(token.split('=')[1])
                        else:
                            imp = float(tokens[k + 1])

            # Comment out the card if IMP = 0
            if imp_found and imp == 0:
                for line_cell in lines_cell:
                    lines_out.append('c ' + line_cell + '\n')
            else:
                for line_cell in lines_cell:
                    lines_out.append(line_cell + '\n')

        # Surface card
        elif num_blank_lines == 1:
            lines_out.append(line + '\n')

        # Data card
        elif num_blank_lines == 2:
            lines_out.append(line + '\n')

    # Write the mcnp2cad input file
    writer = open(inp_file, 'wb')
    for line in lines_out:
        writer.write(line)
    writer.close()

# Find all the files in directories called "Inputs_native"
inp_orig_dirs = []
inp_orig_files = []
for root, dirnames, filenames in os.walk('.'):
    if os.path.basename(root) == 'Inputs_native':
        inp_orig_dirs.append(root)
        for f in filenames:
            inp_orig_files.append(os.path.join(root, f))

# Create the "Inputs_mcnp2cad" directories where the new input files will be placed
for inp_orig_dir in inp_orig_dirs:
    inp_dir = os.path.join(os.path.dirname(inp_orig_dir), 'Inputs_mcnp2cad')
    if not os.path.exists(inp_dir):
        os.makedirs(inp_dir)

for inp_orig_file in inp_orig_files:
    strip_imp0_from_inp(inp_orig_file)
