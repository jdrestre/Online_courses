#!/usr/bin/python

lista = list(range(5, 15, 2))
indice = 0
for indice, recorrer in enumerate(lista):
    lista[indice] *= 10
print(lista)
