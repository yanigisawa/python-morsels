# My Solution
# def parse_ranges(r):
#     for token in r.split(","):
#         if "-" not in token:
#             yield int(token)
#             continue
#         if "->" in token:
#             arrow = token.find("->")
#             yield int(token[:arrow])
#             continue
#         start, end = token.split("-")
#         start, end = int(start), int(end)
#         for x in range(start, end + 1):
#             yield x


# Proposed solution
def parse_ranges(ranges):
    for token in ranges.split(","):
        start, sep, end = token.partition("-")
        if end.startswith(">") or not sep:
            yield int(start)
        else:
            yield from (x for x in range(int(start), int(end) + 1))

