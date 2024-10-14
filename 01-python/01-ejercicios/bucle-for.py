"""
# FOR
variable in elemento iterable (lista, rango, etc)
    Bloque de instrucciones
    
"""

contador = 0
resultado = 0

for contador in range(0,10):
    print('Voy por el', str(contador))
    
    resultado += contador
    
print(f"El resultado es: {resultado}")

# Ejemplo con tablas de multiplicar
print("\n######## Ejemplo ###############")

numero_usuario = int(input("De que numero quieres ver la tabla?: "))

if numero_usuario < 1:
    numero_usuario = 1
    
print(f"\n##Tabla de multiplicar del numero: {numero_usuario}##")

for numero_tabla in range(1, 11):
    print(f"{numero_usuario} x {numero_tabla} = {numero_usuario*numero_tabla}")
else:
    print("Tabla finalizada.")