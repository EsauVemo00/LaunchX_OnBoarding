# Kata 5
# Ejercicio 1.
# Usar operaciones matemáticas
distTierra=149597870 #km
distJupiter=778547200 #km
distPlanetaskm=distTierra-distJupiter
distPlanetasmillas=distPlanetaskm*0.621
print(distPlanetaskm)
print(distPlanetasmillas)

# Ejercicio 2.
# Convierte cadenas en números y usar abs
distPlaneta_1=input('¿Cuál es la distancia de tu primer planeta al Sol en km? ')
distPlaneta_2=input('¿Cuál es la distancia de tu segundo planeta al Sol en km? ')
distPlaneta_1int=int(distPlaneta_1)
distPlaneta_2int=int(distPlaneta_2)
distPlanetaskm=abs(distPlaneta_1int-distPlaneta_2int)
distPlanetasmillas=distPlanetaskm*0.621
print(f'La distancia entre los planetas son\n{distPlanetaskm} km\n{distPlanetasmillas} millas')