def decor(func):
    def _decor():
        print(f'{func()} decorated!')
    return _decor

@decor
def my_name():
    return 'Dimas'

@decor
def names():
    return 'manyNames'

my_name()
names()


print(list(range(2,11,2)))