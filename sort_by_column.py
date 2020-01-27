# Hey!

# This week I'd like you to write a command-line program, sort_by_column.py that will read a CSV file, sort it by a given column number, and print out the resulting sorted rows.

# Given the following CSV file, called colors.csv:

# red,4
# blue,3
# green,8
# purple,1
# Calling sort_by_column.py to sort by the first column and then by the second columns would look like this:

# $ python sort_by_column.py colors.csv 0
# blue,3
# green,8
# purple,1
# red,4
# $ python sort_by_column.py colors.csv 1
# purple,1
# blue,3
# red,4
# green,8
# Note that sort_by_column.py should print out the resulting sorted CSV file, but should not change the original CSV file.

# Bonus 1

# For the first bonus, I'd like you to accept multiple columns to sort by. ✔️

# For example given this cars.csv file:

# 2011,Volkswagen,Golf
# 2013,Toyota,Prius
# 2011,Toyota,Corola
# 2012,Volkswagen,Golf
# 2011,Toyota,Prius
# Sorting on the first and third columns would work like this:

# $ python sort_by_column.py cars.csv 0 2
# 2011,Toyota,Corola
# 2011,Volkswagen,Golf
# 2011,Toyota,Prius
# 2012,Volkswagen,Golf
# 2013,Toyota,Prius
# And sorting on the first, second, and third columns would work like this:

# $ python sort_by_column.py cars.csv 0 1 2
# 2011,Toyota,Corola
# 2011,Toyota,Prius
# 2011,Volkswagen,Golf
# 2012,Volkswagen,Golf
# 2013,Toyota,Prius
# Bonus 2

# For the second bonus, I'd like you to accept a --with-header argument that will treat the first row as a header by keeping it in place. ✔️

# So if cars.csv looked like this:

# Year,Make,Model
# 2011,Volkswagen,Golf
# 2013,Toyota,Prius
# 2011,Toyota,Corola
# 2012,Volkswagen,Golf
# 2011,Toyota,Prius
# Our program would allow for this:

# $ python sort_by_column.py cars.csv --with-header 1 2 0
# Year,Make,Model
# 2011,Toyota,Corola
# 2011,Toyota,Prius
# 2013,Toyota,Prius
# 2011,Volkswagen,Golf
# 2012,Volkswagen,Golf
# Bonus 3

# For the third bonus, I'd like you to accept an optional column type to allow customizing the way columns are sorted. The accepted column types should include str (the default) and num (which will sort columns as if they are numeric). ✔️

# Given a colors.csv file like this:

# red,4
# yellow,3
# blue,10
# green,8
# purple,1
# Sorting based on the second column, numerically should work like this:

# $ python sort_by_column.py colors.csv 1:num
# purple,1
# yellow,3
# red,4
# green,8
# blue,10
# Note that 10 would come before 3 if sorting columns as strings and not as numbers.

import argparse
import csv
import sys


def main(args):
    lines = []
    with open(args.csv_file, "r") as f:
        reader = csv.reader(f, delimiter=",", quotechar='"')
        if args.header:
            headers = next(reader)
        for row in reader:
            lines.append(row)

    def sort_key_func(item):
        sort_item = []
        for x in args.integers:
            try:
                col = int(x)
            except:
                col, t = x.split(":")
                col = int(col)
                if t == "num":
                    sort_item.append(int(item[col]))
                    continue
            sort_item.append(item[col])

        return tuple(sort_item)

    lines_sorted = sorted(lines, key=sort_key_func)
    writer = csv.writer(sys.stdout, quotechar='"')
    if args.header:
        writer.writerow(headers)

    for line in lines_sorted:
        writer.writerow(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sort CSV.")
    parser.add_argument("csv_file", help="file name")
    parser.add_argument(
        "integers", metavar="N", nargs="+", default="0", help="sort columns"
    )
    parser.add_argument(
        "--with-header",
        dest="header",
        action="store_const",
        default=False,
        const=True,
        help="Parse headers from csv",
    )

    args = parser.parse_args()
    # print(args.csv_file)
    # print(args.integers)
    main(args)
