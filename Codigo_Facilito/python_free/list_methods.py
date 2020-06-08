lista = [1, "Dos", 3]

buscar = "Dos"

if buscar in lista:
    print(lista.index(buscar))
else:
    print("no esta elemento")

print (lista)

lista.append("Nuevo elemento")
print (lista)

lista = [1, "Dos", 3]
print(lista.count(3))

print(lista)
lista.insert(2, "New")
print(lista)


lista = [1, "Dos", 3]
print(lista)
iterati = "Cadena"
lista.extend(iterati)
print(lista)


lista = [1, "Dos", 3]
print(lista)
print(lista.pop(2))
print(lista)

lista = [1, "Dos", 3]
print(lista)
lista.remove(3)
print(lista)

lista = [1, "Dos", 3]
print(lista)
lista.reverse()
print(lista)

