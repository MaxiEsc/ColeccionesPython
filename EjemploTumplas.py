# Las tuplas comparten las idea de estructura de datos como las listas pero con la diferencia de las mismas sin inmutables estas son colecciones de datos ordenados
# Una vez ya creada la tupla es imnmodificables son datos mas esticos para la utilizar en cuanto a su redimencionamiento y las edicion de las mismas.
# Su sintaxis se suele dar de la siguiente manera:
# tupla = (elem1,elem2,elem3....elemX)
# tupla = elem1,elem2,elem3....elemX.
# Estas mismas no tienen restricciones con los tipos de datos en cuestion, por lo que es posibles encontrarlas con datos de numeros enteros, incluso una lista y demas.

print('--> Manejo de Tuplas <--')

mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
# No podemos modificar una tupla
#mi_tupla[0] = 10
#mi_tupla.append(6)

# Iteramos los elementos de una tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# Crear una tupla para una coordenada x,y
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\nCoordenada en el eje x: {coordenadas[0]}')
print(f'Coordenada en el eje y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'Tupla de un elemento: {tupla_un_elemento}')

# Tupla anidada
tuplas_anidada = (1, (2,3), (4,5))
print(f'Segundo elemento tupla anidada: {tuplas_anidada[1]}')