from itertools import cycle


class CyclicList:
    def __init__(self, iterable):
        self._cycle = iterable

    def __len__(self):
        return len(self._cycle)

    def append(self, val):
        self._cycle.append(val)

    def pop(self, index=-1):
        return self._cycle[index]

    def __getitem__(self, index):
        if isinstance(index, slice):
            end = len(self._cycle)
            if index.start is not None and index.start < 0:
                end = 0
            if index.stop is not None and index.stop > end:
                end = index.stop
            begin = index.start if index.start is not None else 0
            return [self[x] for x in range(begin, end)]

        try:
            return self._cycle[index]
        except IndexError:
            add_index = abs(index) - len(self._cycle)
            while add_index >= len(self._cycle):
                add_index -= len(self._cycle)
            add_index = add_index if index > 0 else -add_index
            return self._cycle[add_index]

    def __setitem__(self, index, val):
        try:
            self._cycle[index] = val
        except IndexError:
            self._cycle[int(index / len(self._cycle))] = val

    def __iter__(self):
        return cycle(self._cycle)
