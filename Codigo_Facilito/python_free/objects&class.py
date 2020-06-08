class Humano:
    def __init__(self, edad):
        self.edad = edad
        print('i am a new object')
    
    def hablar(self, mensaje):
        print(self.edad)
        print(mensaje)

pedro = Humano(30)
print(type(pedro))
raul = Humano(25)

print('Soy Pedro y tengo {} años'.format(pedro.edad))
print('Soy Raul y tengo {} años'.format(raul.edad))


pedro.hablar('Hola Pedro')
print(type(pedro.hablar))
raul.hablar('Hola Raul')
