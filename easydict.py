class EasyDict(dict):
    def __init__(self, _dict={}, normalize=False, **kwargs):
        self["normalize"] = normalize
        for key in kwargs.keys():
            self[key] = kwargs[key]

        self.update(_dict)
        for key in _dict.keys():
            self[key] = _dict[key]

    def __getattr__(self, name):
        if name not in self and not self["normalize"]:
            raise AttributeError

        try:
            return self[name]
        except KeyError:
            alt_key = name.replace("_", " ")
            if alt_key not in self.keys():
                raise AttributeError
            return self[alt_key]

    def __setattr__(self, name, value):
        if self["normalize"]:
            name = name.replace("_", " ")
        self[name] = value
