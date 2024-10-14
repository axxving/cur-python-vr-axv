"""
    Ejercicio 10
    
        - Pide las notas de 15 alumnos y nos debe de decir cuantos alumnos han aprobado y cuantos han reprobado
"""

totalAlumnos = []
aprobados = []
reprobados = []

while (len(totalAlumnos) <= 15):
    calificacion = int(input("Ingrese la nota del alumno: "))
    totalAlumnos.append(calificacion)

print("Calculando notas")

for nota in totalAlumnos:
    if nota <= 6:
        aprobados.append(nota)
    elif nota >= 7:
        reprobados.append(nota)

print("Alumnos aprobados: ", len(aprobados))
print("Alumnos reprobados: ", len(reprobados))