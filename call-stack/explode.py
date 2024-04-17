import logging


def foo():
    y = 57
    a = 'hello'
    try:
        bar()
    except TypeError:
        print('Ouch bar')
    print('done foo')


def bar():
    x = 33
    v = 99
    baz()
    print('done bar')

def baz():
    foo = 999
    try:
        bam()
    except ValueError:
        print('Ouch bam')
    print('done baz')

def bam():
    data = {"here": "is", "some": "data"}
    raise RuntimeError('oh dear')


if __name__ == '__main__':
    foo()
