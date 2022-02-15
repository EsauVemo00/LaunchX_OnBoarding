# Módulo 9: Uso de funciones en Python
# Ejercicio 1: Trabajar con argumentos en funciones

# Función para tres lecturas de combustible y muestre el promedio

def combustible(*args):
    size = len(args)
    suma = sum(args)
    return suma,size
    # print(prom)

# Función para el prom
def prome(suma1,size):
    prom = suma1/size
    return prom

# Llamamos a la función
suma1 = combustible(50,25,75)
prom = prome(suma1[0],suma1[1])
# print(suma1)
print(prom)

# Ejercicio 2: Trabajo con argumentos de palabra clave

# Función con informe preciso de la misión.
def mission_inform(**inform):
    print(f"Informe preciso de la misión: \n")
    for title,data in inform.items():
        print(f"{title}: {data}")
    # print(inform)

# Escribe tu nueva función
mission_inform(PreTime='11:25',FlyTime='5:00',Destiny='Moon',ExtTank='500',IntTank='500')
