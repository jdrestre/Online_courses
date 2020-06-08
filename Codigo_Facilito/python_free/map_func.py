""" def operador(n, m):
    return n + m   

l1 = [1, 2, 3, 4]
t1 = (9, 8, 7, 6)
lr = map(operador, l1, t1)

print(l1)
print(t1)
print(lr) """

""" def operador(n, m):
    if n == None or m == None:
        return 0
    return n + m   

l1 = [1, 2, 3, 4]
t1 = (9, 8, 7)
lr = map(operador, l1, t1)

print(l1)
print(t1)
print(lr) """

def operador(n, m):
    if n == None or m == None:
        return 0
    return n + m

s1 = "Hola"
s2 = "Mundo"
lr = (map(operador, s1, s2))

print(s1)   
print(s2)
print(list(lr))
