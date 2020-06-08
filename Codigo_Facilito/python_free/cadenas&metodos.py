t = ("h", "o", "l", "a")
o = ";"
s = "Hola mundo"

print(len(s))
print(s.count('o', 0, len(s)))
print(s.lower())
print(s.upper())
print(s.replace('o', 'x', 2))
print(s.split('a'))
print(s.find('a'))
print(s.rfind('a'))
print(o.join(t))
