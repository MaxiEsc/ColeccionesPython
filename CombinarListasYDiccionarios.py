#Ejercicios de listas y Diccionarios con operaciones combinadas para acceder desde distintos perspectivas.

print('--> Listas y Diccionarios <--')

personas = [
    {
        'nombre': 'Regina',
        'apellido': 'Flores',
        'edad': 21
    },
    {
        'nombre': 'Alejandro',
        'apellido': 'Reyes',
        'edad': 32
    }
]

print(personas)

# Acceder a un diccionario desde una lista con esto se puede acceder a la llave de nombre, apellido y edad.
print(f'''Detalle del primer elemento de la lista:
    Nombre: {personas[0].get('nombre')}
    Apellido: {personas[0].get('apellido')}
    Edad: {personas[0].get('edad')}''')

# Recorrer los elementos de la lista
print()
# El metodo enumarate() permite enumerar cada uno de los resgistros del diccionario de personas
# de modo tal que los que nos devolveri un resultado mas enumarado desde 0
# No solo trabaja con listo si no funciona con mas tipos de datos.
for contador, persona in enumerate(personas):
    print(f'{contador + 1} - Persona: {persona}')
    #print(f'Detalle: Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}')

