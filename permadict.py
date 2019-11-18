class PermaDict(dict):
    def __init__(self, *args, silent=False, **kwargs):
        super(PermaDict, self).__init__(*args, **kwargs)
        self.should_raise = True
        self.silent = silent

    def __setitem__(self, key, value):
        if self.silent and key in self.keys():
            return

        if key in self.keys() and self.should_raise:
            raise KeyError
        super(PermaDict, self).__setitem__(key, value)

    def force_set(self, key, value):
        self.should_raise = False
        self[key] = value
        self.should_raise = True

    def update(self, *args, force=False, **kwargs):
        if not args:
            super(PermaDict, self).update(**kwargs)
            return
        for item in args[0]:
            if item in self.keys():
                raise KeyError
            if len(item) == 2:
                self[item[0]] = item[1]

        if self.silent and not force:
            return

        super(PermaDict, self).update(*args, **kwargs)
