# Prints values and column in tabular form. Values and columns should be in string format
# Value => list of list (2d lists). The first dimension contains values for a single entry.
#          The second dimension contains each entry.
# Column => List of column names.
# value = [ [John, 1 , True], [Titer, 2 , False]] are 2 entries


def print_table(values, columns):
    num_columns = len(columns)
    if(num_columns == 0):
        print("NO COLUMNS")
        exit(1)

    # Find max width

    len_li = []
    for x in columns:
        len_li.append([len(x)])

    for x in values:
        for i, y in enumerate(x):
            len_li[i].append(len(y))

    max_li = []
    for x in len_li:
        max_li.append(max(x) + 2)

    line = "+"
    for x in max_li:
        line = line + (("-"*x) + "+")
    print(line)

    cols = ""
    for i, x in enumerate(columns):
        empty_width = max_li[i] - len(x) - 1
        cols = cols + "| " + x + " "*empty_width
    cols = cols + "|"
    print(cols)
    print(line)

    if (len(values) == 0):
        return

    for x in values:
        cols = ""
        for i, y in enumerate(x):
            empty_width = max_li[i] - len(y) - 1
            cols = cols + "| " + y + " "*empty_width

        cols = cols + "|"
        print(cols)
    print(line)
