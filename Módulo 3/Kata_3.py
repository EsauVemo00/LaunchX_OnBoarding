# Ejercicio de alarma de un asteroide con funciones if, else, elif
# Ejercicio 1
# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false.
VelAste=input('Cuál es la velocidad del asteroide en km/s: ')
if int(VelAste)>25:
    print('PELIGRO ASTEROIDE MUY RÁPIDO')
else:
    print('Continua tu vida normal :D')

# Ejercicio 2
# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False
VelAste=input('Cuál es la velocidad del asteroide en km/s: ')
if int(VelAste)>=20:
    print('Ciudadanos pueden avistar un asteroide en el cielo')
else:
    print('Continua tu vida normal :D') 

# Ejercicio 3
# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.
VelAste=input('Velocidad del asteroide en km/s: ')
SizeAste=input('Tamaño del asteroide en metros (m): ')
if int(SizeAste)<=25:
    if int(VelAste)<26 and int(VelAste)<20:
        print('Continua con tu vida normal :D')
    elif int(VelAste)>25:
        print('Peligro asteroide pequeño (Amenaza leve)')
    else:
        print('Asteroide visible en el cielo')
elif int(SizeAste)>25 and int(SizeAste)<1000:
    if int(VelAste)<26 and int(VelAste)<20:
        print('Continua con tu vida normal :D')
    elif int(VelAste)>25:
        print('PELIGRO ASTERORIDE (Amenaza alta)')
    else:
        print('Asteroide visible en el cielo')