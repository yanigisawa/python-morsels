def add_lists(existing, other):
    if type(existing) is int:
        return existing + other

    if len(existing) != len(other):
        raise ValueError
    return [add_lists(existing[x], other[x]) for x in range(len(existing))]


def add(*matrices):
    result = []

    rows, cols = len(matrices[0]), len(matrices[0][0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for m in matrices:
        result = add_lists(result, m)

    return result
