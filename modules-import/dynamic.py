_attrs = ['csv', 'importlib', 'inspect']

def __dir__():
    return _attrs

def __getattr__(name):
    if name not in _attrs:
        raise AttributeError(name)

    print(f'Importing {name!r} for the first time')
    import sys
    module = sys.modules[__name__]

    attr = __import__(name)
    setattr(module, name, attr)
    return attr
