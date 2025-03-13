# En este caso son una coleccion de datos ordenados (3,7+) Estos se almacena en forma de llave clave valor. Es una estructura muy util cuando se necesita
# asociar conjunto de valores con un conjunto.
# La sintaxis de los diccionarios se suelen dar como: diccionario= { clave1:valor1; clave2:valor2 }

print('--> Diccionarios en Python <--')

# Creamos un dict de persona con clave y valor
persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'México'
}
print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona["nombre"]}')
print(f'Edad: {persona.get("edad")}')
print(f'Ciudad: {persona.get("ciudad")}')


# Modificar un valor del diccionario, Si la llave edad dentro del diccionario no se encuentra esta se estaria agregando.
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar un nuevo elemento por ejemplo la llave de profesion Por lo que es importante que todavia estamos agregando subclaves
persona['profesion'] = 'Ingeniero'
print(f'Diccionario de persona: {persona}')

# Eliminar un elemento, para eliminar la llave del diccionario persona
del persona['ciudad']
print(f'Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'Diccionario de persona: {persona}')

# Iterar los elementos de un diccionario (llave, valor) lo recorremos como si fuera una tupla en cuestion.
#Es interesante por que para ubicar los elementos utilizamos la estructura de tupla.
#Entonces podemos utilizar .items() para recuperar los elementos de lleve valor
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

# Obtener los valores se puede utilizar la funcion values() para obtener una lista de valores
# con esto podemos devolver los datos de la funcion en cuestion.
print(f'\nValores del diccionario: ')
for valor in persona.values():
    print(f'- Valor: {valor}')

# Obtener las llaves del diccionario en cuestion.
# Y el elemento .keys() para recuperar
print(f'Impresión de las llaves del diccionario:')
for llave in persona.keys():
    print(f'- {llave}')