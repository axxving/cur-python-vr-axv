"""
    Ejercicio 07
    
        - Sacar el porcentaje de un numero, pide numero y pide porcentaje
"""

# Sacar el porcentaje de un numero, pide numero y pide porcentaje
numero = int(input('A que numero quieres que le saque el porcentaje?: '))
porcentaje = int(input('De cuanto quieres que sea el porcentaje?: '))
porcentaje = (porcentaje / 100) * numero
print(f'El porcentaje de {numero} es {porcentaje}')
