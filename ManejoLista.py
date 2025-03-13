#Comenzamos con listas
#Las listas nos disponen de la restricciones de tipo de dato.
print('--> Manejo de Listas <--')

mi_lista = [5, 3, 7, 9, 3]
print(f'{mi_lista} -> Lista original')

# Largo de una lista
print(f'Largo de la lista: {len(mi_lista)}')

# Acceder a los elementos de la lista por indice
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
#  | 0 | 1 | 2 | 3 | 4 | orden de los mismos
#  | 5 | 3 | 7 | 9 | 3 | Numero en lista
#                    |

# Tambien se pueden acceder con indice negativo, eso solo mueve el puntero.
#  | 0 | 1 | 2 | 3 | 4 | orden de los mismos
#  | 5 | 3 | 7 | 9 | 3 | Numero en lista
#            |
print(f'Accedemos al valor del indice -1: {mi_lista[-3]}')

# Modificar los elementos de una lista con seleccionar el indice del mismo
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

# Agregar un nuevo elemento al final de la lista con append()
mi_lista.append(6)
print(f'{mi_lista} -> Se agregó el elemento 6')

# Añadir un nuevo elemento en un indice especifico con insert desde el indice y que numero.
mi_lista.insert(2, 15)
print(f'{mi_lista} -> Se añadió el valor de 15 en el índice 2')

# Eliminar elementos de una lista
# usando el metodo remove() y busqueda de la coincidencia.
mi_lista.remove(5)
print(f'{mi_lista} -> Se removió el valor 5')
# Removemos por indice con el metodo pop()
mi_lista.pop(1) # Remueve el elemento del indice 1 En otras palabras podemos eliminar el elemento deseado buscaso mediante el indice.
print(f'{mi_lista} -> Se eliminó el índice 1')
# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} -> Se eliminó el índice 2')

# Obtener sublistas
sublista = mi_lista[1:3]  # genera una sublista del indice 1 al 2 (3 no se incluye)
#Para el contexto de las sublistas es simplemente tomar elementos de la lista ya existen en un nueva lista
#  | 10 | 7 | 3 | 6 | Numero en lista
#      { | }{ | }  Con la notacion [1:3]
#      | 7 | 3 | =
print(f'Sublista [1:3]: {sublista}')