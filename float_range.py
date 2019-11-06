class float_range:
    """Return "partially evaluated" version of given function/arguments."""

    def __init__(self, *args, **kwargs):
        if len(args) > 3:
            raise TypeError
        if len(args) < 1:
            raise TypeError
        self.start, self.end, self.step = 0, 0, 1
        if len(args) == 1:
            self.end = args[0]
        if len(args) == 2:
            self.start, self.end = args
        if len(args) == 3:
            self.start, self.end, self.step = args

    def __iter__(self):
        self.n = self.start
        return self

    def __next__(self):
        if self.should_stop():
            raise StopIteration

        tmp = self.n
        self.n += self.step
        return tmp

    def is_empty(self):
        if self.start > self.end and self.step > 0:
            return True
        if self.start < self.end and self.step < 0:
            return True
        return False

    def __reversed__(self):
        i = self.start + (len(self) - 1) * self.step
        for _ in range(len(self)):
            yield i
            i -= self.step

    def __len__(self):
        if self.is_empty():
            return 0
        return round(abs((self.end - self.start) / self.step))

    def should_stop(self):
        if self.is_empty():
            return True
        if self.end < self.start:
            return self.end >= self.n
        return self.n >= self.end

    def __hash__(self):
        return hash(tuple((self.start, self.end, self.step)))

    def __eq__(self, other):
        try:
            return len(self) == len(other)
        except TypeError:
            return hash(self) == other

        # return (
        #     self.start == other.start
        #     and self.end == other.end
        #     and self.step == other.step
        # )

    # def __call__(self):

    #     return []  # self.func(*self.args, *more_args, **all_kwargs)
