import os

def write_tokens_mcnp(writer, tokens, max_length = 80):
    lines = []
    line = tokens[0]
    for token in tokens[1:]:
        if len(line) + len(token) > max_length - 1:
            lines.append(line)
            line = '     ' + token
        else:
            line += ' ' + token
    lines.append(line)
    for line in lines:
        writer.write(line + '\n')

def get_tokens_in_def(lines_all, start_line):
    num_lines = len(lines_all)
    lines = [lines_all[start_line]]
    continue_line = False
    for ii in range(start_line + 1, num_lines):
        line = lines_all[ii]
        if not line:
            break
        if (continue_line or line.startswith('     ') or
            line.split()[0].lower() == 'c'):
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
    num_lines_card = len(lines)

    tokens = []
    for line in lines:
        if line.split()[0] == 'c':
            continue
        for token in line.split():
            if token.startswith('$') or token.startswith('&'):
                break
            tokens.append(token)

    return tokens, num_lines_card

def parse_floats(tokens, num_entries):
    floats = []
    for token in tokens:
        token = token.lower()
        if token[-1] == 'j':
            if token[:-1]:
                num_zero = int(token[:-1])
            else:
                num_zero = 1
            for ii in range(num_zero):
                floats.append(0)
        elif token[-1] == 'r':
            num_repeat = int(token[:-1])
            for ii in range(num_repeat):
                floats.append(floats[-1])
        elif token[-1] == 'i':
            num_interp_lin = int(token[:-1])
        elif token[-1] == 'ilog':
            num_interp_log = int(token[:-4])
        elif token[-1] == 'm':
            mult = float(token[:-1])
            floats.append(floats[-1] * mult)
        else:
            floats.append(float(token))
    for ii in range(num_entries - len(floats)):
        floats.append(0.)
    return floats

def read_block(lines_all, block):
    num_lines_total = len(lines_all)
    block_data = []

    # Loop over all the lines in the original input file (skip the title card)
    num_blank_lines = 0
    num_lines_card = 0
    i = 1
    while i < num_lines_total - num_lines_card:
        i += num_lines_card
        line = lines_all[i]
        num_lines_card = 1

        if line.strip() == '':  # Blank line
            num_blank_lines += 1
            if num_blank_lines > block:  # The block of interest has ended
                break
            continue
        elif num_blank_lines < block:  # Haven't reached block of interest yet
            continue
        elif line.split()[0].lower() == 'c':  # Comment line
            continue

        # Get tokens for the line and any continuation lines
        tokens, num_lines_card = get_tokens_in_def(lines_all, i)

        # Load the data into the dictionary
        block_data.append([])
        for token in tokens:
            block_data[-1].append(token)

    return block_data

def strip_imp0_from_inp(inp_orig_file):
    # Read input from file
    reader = open(inp_orig_file, 'r')
    lines_in = reader.readlines()
    reader.close()

    # Strip trailing whitespace
    for i, line in enumerate(lines_in):
        lines_in[i] = line.rstrip()
    num_lines = len(lines_in)

    # Read all the cards
    title_card = lines_in[0]
    cell_cards = read_block(lines_in, 0)
    surf_cards = read_block(lines_in, 1)
    data_cards = read_block(lines_in, 2)
    num_cells = len(cell_cards)
    num_surfs = len(surf_cards)
    num_datas = len(data_cards)

    # Get info from data cards that needs to be appended to cell cards instead
    cell_data_types = ['imp', 'fcl', 'elpt']
    cell_data = {}
    for data_card in data_cards:
        for cell_data_type in cell_data_types:
            if not data_card[0].startswith(cell_data_type):
                continue
            cell_data[data_card[0]] = parse_floats(data_card[1:], num_cells)

    # Append data from data cards to cell cards as appropriate
    for i, cell_card in enumerate(cell_cards):
        for cell_data_type in sorted(cell_data):
            val = cell_data[cell_data_type][i]
            if (val > 0 or cell_data_type.startswith('imp:') or
                cell_data_type.startswith('elpt:')):
                if val.is_integer():
                    val_str = str(int(val))
                else:
                    val_str = str(val)
                cell_cards[i].append(cell_data_type + '=' + val_str)

    # Figure out which cell cards to write (don't write a card if all its
    # importances are zero)
    write_cell_cards = [False]*num_cells
    for i, cell_card in enumerate(cell_cards):
        for j, token in enumerate(cell_card):
            if not token.startswith('imp:'):
                continue
            if '=' in token:
                imp = float(token.split('=')[1])
            elif cell_card[j + 1] == '=':
                imp = float(cell_card[j + 2])
            else:
                imp = float(cell_card[j + 1])
            if imp > 0:
                write_cell_cards[i] = True

    # Figure out which surface cards to write (don't write a card if it doesn't
    # appear in a cell definition)
    write_surf_cards = [True]*num_surfs
    # This is currently nonfunctional

    # Figure out which data cards to write (don't write a card if its data is
    # being appended to the cell cards instead)
    write_data_cards = [True]*num_datas
    for i, data_card in enumerate(data_cards):
        for cell_data_type in cell_data_types:
            if data_card[0].startswith(cell_data_type):
                write_data_cards[i] = False

    # Put the mcnp2cad input file in the "Inputs_mcnp2cad" directory
    inp_file = os.path.join(os.path.dirname(os.path.dirname(inp_orig_file)),
                            'Inputs_mcnp2cad', os.path.basename(inp_orig_file))

    writer = open(inp_file, 'wb')

    # Add the title card
    writer.write(title_card + '\n')

    # Loop over all the cell cards
    for i, card in enumerate(cell_cards):
        if write_cell_cards[i]:
            write_tokens_mcnp(writer, card)
    writer.write('\n')

    # Loop over all the surface cards
    for i, card in enumerate(surf_cards):
        if write_surf_cards[i]:
            write_tokens_mcnp(writer, card)
    writer.write('\n')

    # Loop over all the data cards
    for i, card in enumerate(data_cards):
        if write_data_cards[i]:
            write_tokens_mcnp(writer, card)

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
