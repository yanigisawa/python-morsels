def get_shape(matrix):
    return [len(l) for l in matrix]


def add(*matrices):
    shape = get_shape(matrices[0])
    if any(get_shape(m) != shape for m in matrices):
        raise ValueError

    return [[sum(values) for values in zip(*rows)] for rows in zip(*matrices)]

