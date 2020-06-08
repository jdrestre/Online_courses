class Prueba(object):
    def __init__(self):
        self.__privado = "Soy privado"
        self.privado = "Soy publico"
    def __metodoPrivado(self):
        print("Soy Privado")
    def metodoPublico(self):
        print("Soy Publico")

obj = Prueba()

print(obj.privado)
print(obj.__privado)
