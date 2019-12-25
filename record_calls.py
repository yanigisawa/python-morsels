import functools

NO_RETURN = "no_return"


class FuncCall:
    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs
        self.exception = None


def record_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        obj = FuncCall(args, kwargs)
        wrapper.calls.append(obj)
        try:
            obj.return_value = func(*args, **kwargs)
            return obj.return_value
        except Exception as e:
            obj.exception = e
            obj.return_value = NO_RETURN
            raise

    wrapper.call_count = 0
    wrapper.calls = []
    return wrapper
