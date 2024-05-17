_attrs = ['csv', 'importlib', 'inspect']

def __dir__():
    return _attrs

def __getattr__(name):
    if name not in _attrs:
        raise AttributeError(name)


