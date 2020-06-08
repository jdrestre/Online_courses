# return and send values
def students():
    return ("Python students")

s = students()
print(s)

def funciones(a, b):
    return a * b

v = funciones(2, 2)
print(v)

# multiple returns
def return_mult():
    return("Juan", "David", 10, [1, 2, 3, 4])

a, b, c, d = return_mult()
print(return_mult())
print("first return argument:", a)

# send values in functions
def multiplication(i, x):
    return i * x

s = multiplication(7, 5)
print(s)
