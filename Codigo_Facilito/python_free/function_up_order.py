""" def prueba(f):
    return f()

def porEnviar():
    return 2 + 2

print(prueba(porEnviar)) """

def seleccion(operacion):
    def suma(n, m):
        return n + m
    def multiplicacion(n, m):
        return n * m
    if operacion == "suma":
        return suma
    elif operacion == "multi":
        return multiplicacion

fGuardada = seleccion("multi")
print(fGuardada(5, 6))
