listaEvaluaciones = [("#1",15),("#2",20),("#3",20),("#4",20),("#5",25)]
listaNotasEstudiante1 = [5.0,4.5,3.5,4.7,3.9]
promedio = 0
for i in range (len(listaNotasEstudiante1)):
    promedio = promedio + (listaEvaluaciones[i][1]*listaNotasEstudiante1[i]/100)


print(promedio)

