#/usr/bin/python3

nota = float(input())

if nota >= 6 and nota <= 10:
    print("pasó")
elif nota < 6 and nota >=0:
    print("perdió")
else:
    print("ingrese valor entre 1 y 10")
