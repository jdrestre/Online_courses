l = [1, 2, 3, -1, 4]
s = ["H", "O", "L", "A"]
l2 = [num for num in l if num > 0]
l3 = (c * num for c in s for num in l if num > 0)

""" print(l)
print(l2)
print(l3)

#print(next(l3))

for letra in l3:
    print(letra)
 """

def factorial(n):
    i = 1
    while n > 1:
        i = n * i
        yield i
        n -= 1

for e in factorial(5):
    print(e)
