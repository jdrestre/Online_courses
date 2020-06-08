class Humano:
    def __init__(self, edad):
        self.edad = edad
        print('i am a new object')
    
    def hablar(self, mensaje):
        print(mensaje)

class Ingeniero(Humano):
    def __init__(self):
        print('Hola')

    def programar(self, language):
        print('Voy a programar en {}'.format(language))

class Abogado(Humano):
    def __init__(self, escuela):
        print('Abogado egresado de: {}'.format(escuela))

    def casos(self, de):
        print('Debo estudiar el caso de {}'.format(de))

class estudioso(Abogado, Ingeniero):
    pass

pepe = estudioso('Eafit')

pepe.hablar('Hola soy heritange multiple')
pepe.programar('C')
pepe.casos('Pedro')
