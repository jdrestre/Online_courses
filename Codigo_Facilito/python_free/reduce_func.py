from functools import reduce
""" s = ('H', 'o', 'l', 'a', '_', 'M', 'u', 'n', 'd', 'o')

def concatenar(a, b):
    return (a + b)

sr = reduce(concatenar, s)

print(type(sr))
print(sr) """


s = (1, 2, 3)

def suma(a, b):
    return (a + b)

sr = reduce(suma, s)

print(type(sr))
print(sr)
