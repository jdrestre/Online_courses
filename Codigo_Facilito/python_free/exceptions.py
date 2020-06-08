""" print("Bienvenido")
try:
    print(4)
except (NameError):
    print("No está definido el nombre")
except (TypeError):
    print("erro de tipo de dato")
except ZeroDivisionError:
    print("No divisible por cero")
else:
    print("no hubo error")
finally:
    print("Me ejecuto siempre")

print("Adios") """


print("Bienvenido")
try:
    print(4)
except (NameError):
    print("No está definido el nombre")

print("Adios")