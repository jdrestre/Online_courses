def funcname(value):
    value *= 3

variable = 15
funcname(variable)
print(variable)

def lista(number):
    for x, i in enumerate(number):
        number[x] *= 3

listas = [50, 100, 150]
print(lista(listas))
