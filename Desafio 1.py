from random import randint
calificaciones=[]
for i in range(5):
    alumno=[]
    for e in range(5):
        alumno.append(randint(1,10))
    calificaciones.append(alumno)
print(calificaciones)