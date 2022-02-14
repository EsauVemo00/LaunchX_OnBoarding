# Módulo 8: Administrar datos con diccionarios
#Ejercicio 1: Crear y modificar un diccionario de Python

# Inicializar variables
planet = {
    'name': 'Mars',
    'moons': 2
}
# Muestra el nombre del planeta y el número de lunas
print(f"El planeta {planet.get('name')} tiene {planet['moons']} lunas")
planet['circunferencia (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}
print(f"El planeta {planet.get('name')} tiene su circunferencia polar de {planet['circunferencia (km)']['polar']} (km)")

# Ejercicio 2: Programación dinámica con diccionarios

# Inicializa el diccionario
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Añade el código para determinar el número de Lunas
moons=0
for val in planet_moons.values():
    moons=moons+val
print(f"El número total de lunas es: {moons}")
#
# Almacerna el número de planetas en una variable denominada planets
planets=0
for pla in planet_moons.keys():
    planets=planets+1
print(f"El total de planetas es: {planets}")

#Calcule el promedio
prom=moons/planets
print(f"El promedio de lunas en los planetas es: {prom}")