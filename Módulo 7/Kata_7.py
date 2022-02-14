# Módulo 7: Estructuras de control
# Ejercicio 1: Creación de un bucle "While"

# Iniciarlizar las variables
from re import I


new_planet = ''
planets = []
# Crear ciclo While
while new_planet.lower() != 'done':
    if new_planet:
        planets.append(new_planet)
    new_planet=input('Ingresa un planeta: ')
# print(f'Los planetas escritos son:\n{planets}')

# Ejercicio 2: Creación de un ciclo "for"
j = 0
for planet in planets:
    j=j+1
    print(f'Planeta #{j} es: {planet}')