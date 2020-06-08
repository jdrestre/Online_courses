class Humano:
    def __init__(self, edad):
        self.edad = edad
        print('i am a new object')
    
    def hablar(self, mensaje):
        print(self.edad)
        print(mensaje)

class Ingeniero(Humano):
    def programar(self, language):
        print('Voy a programar en {}'.format(language))

class Abogado(Humano):
    def casos(self, de):
        print('Debo estudiar el caso de {}'.format(de))

pedro = Ingeniero(30)
raul = Abogado(25)

pedro.programar('Python')
raul.casos('Pedro')

pedro.hablar('Hola Pedro')
raul.hablar('Hola Raul')
