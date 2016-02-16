import os
import time

def write_line(writer, level, text):
    writer.write('  '*level + text + '\n')

def write_html_head(writer, code):
    write_line(writer, 0, '<!DOCTYPE HTML PUBLIC>')
    write_line(writer, 0, '<html>')
    write_line(writer, 1, '<head>')
    write_line(writer, 2, '<title>' + code + ' testing diff summary</title>')
    write_line(writer, 1, '</head>')
    write_line(writer, 1, '<body>')
    write_line(writer, 2, '<h1>' + code + ' testing diff summary</h1>')
    write_line(writer, 2, '<h3>' + datetime_1 + '</h3>')

def write_html_data(writer, suite, ftypes, tests, ndiffs, ctms):
    write_line(writer, 2, '<h2>' + suite + '</h2>')
    write_line(writer, 2, '<table border=\'1\' cellpadding=\'4\' cellspacing=\'0\'>')
    write_line(writer, 3, '<tr>')
    write_line(writer, 4, '<th>Name</th>')
    write_line(writer, 4, '<th align=\'right\'>ctm</th>')
    for ftype in ftypes:
        write_line(writer, 4, '<th align=\'right\'>' + ftype + '</th>')
    write_line(writer, 3, '</tr>')
    for test in tests:
        write_line(writer, 3, '<tr>')
        write_line(writer, 4, '<td>' + test + '</td>')
        if not ctms[test] == '-':
            write_line(writer, 4, '<td align=\'right\'>' + ctms[test] + '</td>')
        else:
            write_line(writer, 4, '<td>' + ctms[test] + '</td>')
        for ftype in ftypes:
            if ftype in ndiffs[test]:
                if ndiffs[test][ftype] > 0:
                    write_line(writer, 4, '<td align="right"><b><font color="red">' + str(ndiffs[test][ftype]) + '</font></b></td>')
                else:
                    write_line(writer, 4, '<td align="right">' + str(ndiffs[test][ftype]) + '</td>')
            else:
                write_line(writer, 4, '<td>-</td>')
        write_line(writer, 3, '</tr>')
    write_line(writer, 2, '</table><br>')

def write_html_tail(writer):
    write_line(writer, 1, '</body>')
    write_line(writer, 0, '</html>')

def write_text_head(writer, code):
    writer.write('%s testing diff summary\n\n' % code)
    writer.write('%s\n\n' % datetime_1)

def write_text_data(writer, suite, ftypes, tests, ndiffs, ctms):
    writer.write('%s\n' % suite)
    writer.write('%-24s%12s' % ('Name', 'ctm'))
    for ftype in ftypes:
        writer.write('%12s' % ftype)
    writer.write('\n')
    for test in tests:
        writer.write('%-24s' % test)
        writer.write('%12s' % ctms[test])
        for ftype in ftypes:
            if ftype in ndiffs[test]:
                writer.write('%12s' % ndiffs[test][ftype])
            else:
                writer.write('%12s' % '-')
        writer.write('\n')
    writer.write('\n')

def write_summary(code, suites):
    folder = 'summaries'
    summary_text = os.path.join(folder, 'summary_' + code + '_' + datetime_2 + '.txt')
    summary_html = os.path.join(folder, 'summary_' + code + '_' + datetime_2 + '.html')

    if not os.path.isdir(folder):
        os.mkdir(folder)

    with open(summary_html, 'wb') as writer:
        write_html_head(writer, code)
    with open(summary_text, 'wb') as writer:
        write_text_head(writer, code)

    for suite in suites:
        results_dir = os.path.join(code, suite, 'Results')
        if not os.path.isdir(results_dir):
            continue

        # Get all test names
        tests = [x[0] for x in os.walk(results_dir)]
        for i, test in enumerate(tests):
            if test == results_dir:
                tests.remove(test)
        for i, test in enumerate(tests):
            tests[i] = tests[i].replace(results_dir + '/', '')
        tests = sorted(tests)

        # Get all diff file types
        ftypes = []
        for test in tests:
            test_dir = os.path.join(results_dir, test)
            files = os.listdir(test_dir)
            for f in files:
                if f.startswith('diff_'):
                    ftype = f.replace('diff_', '')
                    if ftype not in ftypes:
                        ftypes.append(ftype)
        ftypes = sorted(ftypes)

        # Count the number of diffs for each diff file in each test
        ndiffs = {}
        for test in tests:
            test_dir = os.path.join(results_dir, test)
            files = os.listdir(test_dir)
            ndiffs[test] = {}
            for ftype in ftypes:
                f = 'diff_' + ftype
                if not f in files:
                    continue
                ndiffs[test][ftype] = 0
                for line in open(os.path.join(test_dir, f), 'r'):
                    if line[0] == '>' or line[0] == '<':
                        ndiffs[test][ftype] += 1

        # Get the computer time for each test
        ctms = {}
        for test in tests:
            test_dir = os.path.join(results_dir, test)
            ctms[test] = '-'
            for line in open(os.path.join(test_dir, 'screen_out'), 'r'):
                if 'ctm =' in line:
                    ctms[test] = line.split()[2]

        with open(summary_html, 'ab') as writer:
            write_html_data(writer, suite, ftypes, tests, ndiffs, ctms)
        with open(summary_text, 'ab') as writer:
            write_text_data(writer, suite, ftypes, tests, ndiffs, ctms)

    with open(summary_html, 'ab') as writer:
        write_html_tail(writer)

def main():
    global datetime_1, datetime_2
    datetime_1 = time.strftime('%Y/%m/%d  %H:%M:%S')
    datetime_2 = datetime_1.replace('/', '-').replace(':', '-').replace(' ', '_')

    codes = ['DAG-MCNP5', 'FluDAG']
    for code in codes:
        suites = []
        for name in os.listdir(code):
            if os.path.isdir(os.path.join(code, name)) and name[0] != '.':
                if os.path.isdir(os.path.join(code, name, 'Results')):
                    suites.append(name)
        suites = sorted(suites)
        write_summary(code, suites)

main()
