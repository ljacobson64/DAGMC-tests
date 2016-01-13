import os

def write_line(writer, level, text):
    writer.write("  "*level + text + "\n")

def write_html_head(writer):
    write_line(writer, 0, "<!DOCTYPE HTML PUBLIC>")
    write_line(writer, 0, "<html>")
    write_line(writer, 1, "<head>")
    write_line(writer, 2, "<title>Insert title here</title>")
    write_line(writer, 1, "</head>")
    write_line(writer, 1, "<body>")
    write_line(writer, 2, "<h1>Insert title here</h1>")

def write_html_data(writer, suite, ftypes, tests, ndiffs):
    write_line(writer, 2, "<h2>" + suite + "</h2>")
    write_line(writer, 2, "<table border=\"1\" cellpadding=\"4\" cellspacing=\"0\">")
    write_line(writer, 3, "<tr>")
    write_line(writer, 4, "<th>Name</th>")
    for ftype in ftypes:
        write_line(writer, 4, "<th align=\"right\">" + ftype + "</th>")
    write_line(writer, 3, "</tr>")
    for test in tests:
        write_line(writer, 3, "<tr>")
        write_line(writer, 4, "<td>" + test + "</td>")
        for ftype in ftypes:
            if ftype in ndiffs[test]:
                write_line(writer, 4, "<td align=\"right\">" + str(ndiffs[test][ftype]) + "</td>")
            else:
                write_line(writer, 4, "<td>-</td>")
        write_line(writer, 3, "</tr>")
    write_line(writer, 2, "</table><br>")

def write_html_tail(writer):
    write_line(writer, 1, "</body>")
    write_line(writer, 0, "</html>")

def write_text_data(writer, suite, ftypes, tests, ndiffs):
    writer.write("%s\n" % suite)
    writer.write("%-24s" % "Name")
    for ftype in ftypes:
        writer.write("%12s" % ftype)
    writer.write("\n")
    for test in tests:
        writer.write("%-24s" % test)
        for ftype in ftypes:
            if ftype in ndiffs[test]:
                writer.write("%12s" % ndiffs[test][ftype])
            else:
                writer.write("%12s" % "-")
        writer.write("\n")
    writer.write("\n")

suites = ["DAGMC", "Meshtally", "Regression", "VALIDATION_CRITICALITY",
          "VALIDATION_SHIELDING", "VERIFICATION_KEFF"]

summary_text = os.path.join("summaries", "summary.txt")
summary_html = os.path.join("summaries", "summary.html")

with open(summary_html, 'wb') as writer:
    write_html_head(writer)

for suite in suites:
    results_dir = os.path.join(suite, "Results")
    if not os.path.isdir(results_dir):
        continue

    tests = [x[0] for x in os.walk(results_dir)]
    for i, test in enumerate(tests):
        if test == suite + "/Results":
            tests.remove(test)
    for i, test in enumerate(tests):
        tests[i] = tests[i].replace(suite + "/" + "Results/", "")
    tests = sorted(tests)

    ftypes = []
    for test in tests:
        test_dir = os.path.join(results_dir, test)
        files = os.listdir(test_dir)
        for f in files:
            if f.startswith("diff_"):
                ftype = f.replace("diff_", "")
                if ftype not in ftypes:
                    ftypes.append(ftype)
    ftypes = sorted(ftypes)

    ndiffs = {}
    for test in tests:
        test_dir = os.path.join(results_dir, test)
        files = os.listdir(test_dir)
        ndiffs[test] = {}
        for ftype in ftypes:
            f = "diff_" + ftype
            if not f in files:
                continue
            ndiffs[test][ftype] = 0
            for line in open(os.path.join(suite, "Results", test, f), 'r'):
                if line[0] == ">" or line[0] == "<":
                    ndiffs[test][ftype] += 1

    with open(summary_text, 'wb') as writer:
        write_text_data(writer, suite, ftypes, tests, ndiffs)

    with open(summary_html, 'ab') as writer:
        write_html_data(writer, suite, ftypes, tests, ndiffs)

with open(summary_html, 'ab') as writer:
    write_html_tail(writer)
