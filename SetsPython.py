# A diferencia de la tuplas y las listas estos elementos no estan ordenados por lo que hay que asegurarse que los elementos no esten duplicados.
# Los elementos duplicados no se guardaran y se ignoraran dentro del sistema. estos se determinan con {}
# Estos se dan con este ejemplo set = {elem1, elem2, elem3, ... elemX}

#Los Sets

print('--> Manejo de Sets <--')

# Crear un conjunto
p_set = {1, 2, 3, 4, 5, 4}
print(f'Mi set: {p_set}')

# Agregar elementos al set: Este se agregara al sets ignorando el orden
p_set.add(6)
p_set.add(7)

# Intentamos agregar un elemento duplicado y como dice el teorico no se agrega y no pasa nada.
p_set.add(3)

# Eliminar un elemento del conjunto, Permite elimitar mediante elementos por que los indices no existen.
p_set.remove(4)
print(f'Mi set modificado: {p_set}')

# Iterar los elementos del set
for elemento in p_set:
    print(elemento, end=' ')

# Comprobar si existe un elemento en el set
print(f'\nExiste el valor de 1 en el set? {1 in p_set}')

# Obtener la longitud del set
print(f'Longitud del conjunto: {len(p_set)}')