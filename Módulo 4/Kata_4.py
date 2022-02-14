# Kata 4. Ejercicio #1: Transformar cadenas
text="""Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."""

# Dividir el texto
texto_div=text.split(". ")

# Define algunas palabras clave
Key_words="average","temperature","distance"

# Obtener frases que tengan una Key_words
for i in texto_div:
    for j in Key_words:
        if i.find(j)>0:                         # if key_word in sentence:
            print(i.replace('C','Celsius'))     # Se puede usar en vez de la que tengo
                                                # se utiliza un break

# Ejercicio #2: Formateando cadenas
# Datos con los que vas a trabajar
name = "Moon"
gravity = 0.00162 # in kms
planet = "Earth"
# Datos para prueba
#name = "Ganímedes"
#gravity = 0.00143 # in kms
#planet = "Marte"


# creamos el título
titulo=f'\nGravity facts about the: {name}'

# Creamos la plantilla
gms=gravity*1000


#Unión de ambas cadenas
print(titulo.title())
print('--------------------')
print(f'Planet name: {planet}')
print(f'Gravity on {name} is: {gms} m/s2')


# Es como se plantea que se haga
# ANALIZAR CON PRECAUCIÓN
planeta = 'Marte '
gravedad  = 0.00143
nombre = 'Ganímedes'
titulo=f'\nGravity facts about the: {nombre}'
hechos = f"""{'-'*80}
Nombre del planeta: {planeta} 
Gravedad en {nombre}: {gravedad * 1000} m/s2 
"""
template = f"""{titulo.title()} 
{hechos} 
""" 
print(template)

new_template = """
Datos de Gravedad sobre: {nombre}
-------------------------------------------------------------------------------
Nombre del planeta: {planeta}
Gravedad en {nombre}: {gravedad} m/s2
"""
print(new_template.format(nombre='Luna', planeta='Tierra', gravedad=0.00162))