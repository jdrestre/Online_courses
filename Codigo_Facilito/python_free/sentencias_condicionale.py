edad = 19
m_edad = 18

if edad >= m_edad:
    print('Eres mayor de edad')
    if False:
        print('Esto se ejecuta True if')
    else:
        print('Es falso el if')
else:
    print('No eres mayor de edad')
print('Esto se ejectuta siempre fuera')
print('###########')

edad = 15

if edad >= 0 and edad < 18:
    print('eres niño')
elif edad >= 18 and edad < 27:
    print('eres joven')
elif edad >= 27 and edad < 60:
    print('eres adulto')
else:
    print('eres tercera edad')