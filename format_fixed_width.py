# This week I'd like you to write a function, format_fixed_width, that accepts rows of columns (as a list of lists)
# and returns a fixed-width formatted string representing the given rows.

# For example:

# >>> print(format_fixed_width([['green', 'red'], ['blue', 'purple']]))
# green  red
# blue   purple
# The padding between the columns should be 2 spaces. Whitespace on the right-hand
# side of each line should be trimmed and columns should be left-justified.

# Bonus #1

# For the first bonus, allow the padding for columns to be specified
# with an optional padding keyword argument:

# >>> rows = [['Robyn', 'Henry', 'Lawrence'], ['John', 'Barbara', 'Gross'], ['Jennifer', '', 'Bixler']]
# >>> print(format_fixed_width(rows))
# Robyn     Henry    Lawrence
# John      Barbara  Gross
# Jennifer           Bixler
# >>> print(format_fixed_width(rows, padding=1))
# Robyn    Henry   Lawrence
# John     Barbara Gross
# Jennifer          Bixler
# >>> print(format_fixed_width(rows, padding=3))
# Robyn      Henry     Lawrence
# John       Barbara   Gross
# Jennifer              Bixler
# Bonus #2

# For the second bonus, allow column widths to be specified manually with an optional widths keyword argument:

# >>> rows = [["Jane", "", "Austen"], ["Samuel", "Langhorne", "Clemens"]]
# >>> print(format_fixed_width(rows, widths=[10, 10, 10]))
# Jane                    Austen
# Samuel      Langhorne   Clemens
# Bonus #3

# For the third bonus, allow column justifications (left or right) to be specified with with an optional alignments keyword argument. This argument will take lists of 'L' and 'R' strings representing left and right:

# >>> print(format_fixed_width(rows, alignments=['R', 'L', 'R']))
#   Jane              Austen
# Samuel  Langhorne  Clemens
# Hints

# Getting the longest string
# Looping over multiple things at the same time
# Left-justifying strings
# Removing spaces from the end of a line
# Joining rows back together
# A shorthand for creating new lists from old lists
# Bonus 1: making optional function arguments
# Bonus 1: making a string of N whitespace characters
# Bonus 3: Right-justifying strings
# Tests

# Automated tests for this week's exercise can be found here. You'll need to write your function in a module named format_fixed_width.py next to the test file. To run the tests you'll run "python test_format_fixed_width.py" and check the output for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.

# Once you've written a solution for this exercise, submit your solution to track your progress! ✨

# Submit your solution

# You can also view the problem statement for this exercise on the Python Morsels website.

# To make sure you keep getting these emails, please add trey@pythonmorsels.com to your address book.

# If you want to unsubscribe from Python Morsels click here


def get_widths(rows):
    widths = [0 for _ in range(len(rows[0]))]
    for row in rows:
        for i, col in enumerate(row):
            widths[i] = len(col) if len(col) > widths[i] else widths[i]
    return widths


def format_fixed_width(rows, padding=2, widths=None, alignments=None):
    if not len(rows):
        return ""

    if widths is None:
        widths = get_widths(rows)

    if alignments is None:
        alignments = ["L" for row in rows for _ in row]

    result = []
    for row in rows:
        row_str = ""
        for col, width, alignment in zip(row, widths, alignments):
            if alignment == "L":
                row_str += f"{col}".ljust(width + padding)
            else:
                row_str += f"{col}".rjust(width)

        result.append(row_str.rstrip())

    return "\n".join(result)
