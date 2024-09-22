"""
    Ejercicio 07
    
        - Mostrar numeros pares de dos numeros que haya ingresado el usuario
"""

numero_uno = (int(input("Ingresa el primer numero: ")))
numero_dos =(int(input("Ingresa el segundo numero: ")))

if (numero_uno % 2 == 0):
    print(f"{numero_uno} es par")
else:
    print('El numero no es par')

if (numero_dos % 2 == 0):
    print(f"{numero_uno} es par")
else: 
    print('El numero no es par')
    
    