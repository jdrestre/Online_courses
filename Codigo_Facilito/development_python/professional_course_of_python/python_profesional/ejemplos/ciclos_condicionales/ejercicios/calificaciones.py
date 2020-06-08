calificaciones = {'calculo': 9.5, 'algebra': 8, 'fisica': 8.5, 'quimica': 9 }

cal = list(calificaciones.values())
print("El promedio del alumno es:", sum(cal)/len(cal))

listofTuples = sorted(calificaciones.items(), reverse=True, key=lambda x: x[1])
for elem in listofTuples:
    print("La materia con mejor promedio es: ", elem[0])
    break 
