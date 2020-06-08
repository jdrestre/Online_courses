def my_func(num1, num2):
    print(num1 + num2)

my_func(3, 4)

print("###########")

def my_func1(string, t, *someone):
    print(string * t)
    print(someone)
    for cadena in someone:
        print(cadena * t)

my_func1('Hola\n', 4, 'Juan', 'David', 5)

print("###########")

def my_func2(string, t, **someone):
    print(string * t)
    print(someone)
    print('Mi nombre es: {} {}'.format(someone['name'], someone['second']))
    for dic in someone:
        print(dic)

my_func2('Hola\n', 4, name = 'Juan', second = 'David', age = 5)

print("###########")

def my_func3(num1, num2):
    return num1 + num2

sum = my_func3(5, 7)
print(sum)
