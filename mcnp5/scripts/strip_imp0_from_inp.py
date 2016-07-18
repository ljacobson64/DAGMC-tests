import os

def get_lines_and_tokens_in_def(lines_all, start_line):
    num_lines = len(lines_all)
    lines = [lines_all[start_line]]
    continue_line = False
    for ii in range(start_line + 1, num_lines):
        line = lines_all[ii]
        if not line:
            break
        if continue_line or line.startswith('     ') or line.split()[0].lower() == 'c':
            lines.append(line)
        else:
            break
        tokens = line.split()
        for token in tokens:
            if token == '$':
                break
            if token == '&':
                continue_line = True
                break
            continue_line = False
    for line in reversed(lines):
        if line.split()[0] == 'c':
            lines.pop()
        else:
            break

    tokens = []
    for line in lines:
        if line.split()[0] == 'c':
            continue
        for token in line.split():
            if token.startswith('$') or token.startswith('&'):
                break
            tokens.append(token)

    return lines, tokens

def parse_implike_data(imps_str):
    imps = []
    for token in imps_str:
        if token[-1] == 'r':
            num_repeat = int(token[:-1])
            for j in range(num_repeat):
                imps.append(imps[-1])
        elif token[-1] == 'i':
            num_interp_lin = int(token[:-1])
        elif token[-1] == 'ilog':
            num_interp_log = int(token[:-4])
        elif token[-1] == 'm':
            mult = float(token[:-1])
            imps.append(imps[-1] * mult)
        else:
            imps.append(float(token))
    return imps

def read_data_cards(lines_in):
    num_lines = len(lines_in)
    data = {}

    # Loop over all the lines in the original input file
    num_blank_lines = 0
    num_lines_skip = 0
    i = -1
    while i < num_lines - (num_lines_skip + 1):
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
        lines, tokens = get_lines_and_tokens_in_def(lines_in, i)
        num_lines_skip = len(lines) - 1

        # Load the data into the dictionary
        card_type = tokens[0]
        data[card_type] = []
        for token in tokens[1:]:
            data[card_type].append(token)

    return data

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
    data = read_data_cards(lines_in)

    # Get importance data out of the data dictionary
    imps = {}
    for key in data:
        if key[:4] == 'imp:':
            particle_types = key[4:].split(',')
            for particle_type in particle_types:
                imps[particle_type] = parse_implike_data(data[key])

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
            lines, tokens = get_lines_and_tokens_in_def(lines_in, i)
            num_lines_skip = len(lines) - 1

            # Get the cell's importance
            comment_this_line = False
            if imps:  # specified in data cards
                for particle_type in imps:
                    imp = imps[particle_type][cell_index]
                    if imp == 0:
                        comment_this_line = True
            else:  # specified with cell card
                for k, token in enumerate(tokens):
                    if not token.lower().startswith('imp:'):
                        continue
                    if '=' in token:
                        imp = float(token.split('=')[1])
                    elif tokens[k + 1] == '=':
                        imp = float(tokens[k + 2])
                    else:
                        imp = float(tokens[k + 1])
                    if imp == 0:
                        comment_this_line = True

            # Comment out the card if IMP = 0
            for line in lines:
                if comment_this_line:
                    lines_out.append('c ' + line + '\n')
                else:
                    lines_out.append(line + '\n')

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
inp_orig_files = sorted(inp_orig_files)

# Create the "Inputs_mcnp2cad" directories where the new input files will be placed
for inp_orig_dir in inp_orig_dirs:
    inp_dir = os.path.join(os.path.dirname(inp_orig_dir), 'Inputs_mcnp2cad')
    if not os.path.exists(inp_dir):
        os.makedirs(inp_dir)

num_success = 0
num_failure = 0
for inp_orig_file in inp_orig_files:
    try:
        strip_imp0_from_inp(inp_orig_file)
        num_success += 1
        #print 'SUCCESS: ' + inp_orig_file
    except:
        num_failure += 1
        print 'FAILURE: ' + inp_orig_file
print 'Successes: ' + str(num_success) + ', Failures: ' + str(num_failure)
