"""
    Ejercicio 02
    
        - Escribir un programa wue muestre los cuadrados de los 60 primeros numeros naturales. Resolverlo con for y con while
"""

# Usando un bucle for
squares_for = [i**2 for i in range(1, 61)]
print("Cuadrados usando for loop:", squares_for)

# Usando un bucle while
squares_while = []
i = 1
while i <= 60:
    squares_while.append(i**2)
    i += 1
print("Cuadrados usando while loop:", squares_while)

