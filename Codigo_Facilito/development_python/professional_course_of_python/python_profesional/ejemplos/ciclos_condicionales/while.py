numero = 123456789
contador = 0

while numero >= 1:
  contador+=1
  numero = numero / 10
  print(numero)
  #print(contador)
else:
  print("La cantidad de dígiyos del número es ", contador)