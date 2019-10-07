import functools


def inheritors(c):
    subclasses = set([c])
    tmp = [c]
    while tmp:
        parent = tmp.pop()
        for child in parent.__subclasses__():
            subclasses.add(child)
    return subclasses


class suppress:
    def __init__(self, *args):
        exceptions = []
        for a in args:
            exceptions.extend(inheritors(a))

        self.exception_types = exceptions

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with suppress(*self.exception_types):
                return func(*args, **kwargs)

        return wrapper

    def __enter__(self):
        return self

    def __exit__(self, e_type, value, traceback):
        self.exception = value
        self.traceback = traceback
        for c in self.exception_types:
            if e_type in self.exception_types:
                return True

        return False
