from functools import reduce
li = [1, -2, 1, -4]
lo = [5, 3, 6, 7]
s = "Hoola Mundo"

ss = lambda n, m: n * m

print(list(map(ss, li, lo)))
print(list(filter(lambda n: n == 'o', s)))
print(reduce(ss, lo))

print(ss(7, 21))
