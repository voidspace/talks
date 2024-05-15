
def proxy(thing, attrs: list | set):
    attrs = set(attrs)
    class ProxyThing:
        def __getattr__(self, name):
            if name in attrs:
                return getattr(thing, name)
            raise AttributeError(name)
        def __setattr__(self, name, value):
            if name in attrs:
                return setattr(thing, name, value)
            raise AttributeError(name)
        def __delattr__(self, name, value):
            if name in attrs:
                return setattr(thing, name, value)
            raise AttributeError(name)
        def __dir__(self):
            return list(attrs)
    return ProxyThing()
