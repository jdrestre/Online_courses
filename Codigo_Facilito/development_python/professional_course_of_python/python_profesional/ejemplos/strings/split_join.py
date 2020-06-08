lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"
dictio = "'name': 'Juan David', 'last_name': 'Restrepo', 'Age': 41"


separador = "; "
sep = ", "

result = dictio.split(sep)
resultado = lenguajes.split(separador) #resultado es una lista
print(dictio)
print(result)
print(result[1])
string = sep.join(result)
print(string)

#print(resultado)

nuevo_string = separador.join(resultado)
#print(nuevo_string)

texto = """Este es un texto
con
saltos
de

línea"""

resultado = texto.splitlines()
#print(resultado)