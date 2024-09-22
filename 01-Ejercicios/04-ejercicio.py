"""
    Ejercicio 02
    
        - Pedir dos numeros al usuario y hacer todas las operaciones basicas de una calculadora
"""

numero_uno = int(input('Escribe el primer numero: '))
numero_dos = int(input('Escribe el segundo numero: '))
print('#### Elige la operacion: ####')
print("""
       1 - Suma
       2 - Resta
       3 - Multiplicacion
       4 - Division
        
      """)
operacion = int(input('Selecciona la operacion a realizar: '))



respuesta = 0

if (operacion == 1):
    respuesta = numero_uno + numero_dos
    print("La respuesta es: ", respuesta )
elif (operacion == 2):
    respuesta = numero_uno - numero_dos
    print("La respuesta es: ", respuesta )
elif (operacion == 3):
    respuesta = numero_uno * numero_dos
    print("La respuesta es: ", respuesta )
elif (operacion == 4):
    respuesta = numero_uno / numero_dos
    print("La respuesta es: ", respuesta )