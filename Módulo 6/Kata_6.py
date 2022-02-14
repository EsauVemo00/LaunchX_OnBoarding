# Kata 6
# Ejercicio 1: Crear y usar listas de Python.
planets=['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Urano','Neptuno']
print(f'En el sistema solar tenemos {len(planets)} planetas')
planets.append('Plutón')
print(f'Mentira! Tenemos {len(planets)} planetas con {planets[8]}')

# IMPORTANTE
# En vez de utilizar (planets[8]) utilizar el número negativo
# (planets[-1]) porque me mandará directamente el úlitmo 
# cuando el 8 puede ser o no el úlitmo dependiendo de la cantidad
# de datos.

# Ejercicio 2: Trabajando con datos de una lista.
planets=['Mercurio','Venus','Tierra','Marte','Jupiter','Saturno','Urano','Neptuno']
Pinput=input('Escribe el nombre de un planeta\n(Escribe la primer letra en mayúsculas)\n ')
Pindex=planets.index(Pinput)
print(f'''Los planetas más cercanos al Sol desde: {planets[Pindex]}
son {planets[0:Pindex]}\n''')
print(f'''Los planetas más alejados al Sol desde: {planets[Pindex]}
son {planets[Pindex+1:]}\n''')