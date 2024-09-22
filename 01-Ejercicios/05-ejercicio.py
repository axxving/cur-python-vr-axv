"""
    Ejercicio 02
    
        - Hacer un conteo de numeros hasta el numero indicado
"""
numeroUno = int(input("Ingresa hasta que numero quieres que cuente: "))

for numero in range(0, numeroUno+1):
    print(f"Cuento: ", numero)