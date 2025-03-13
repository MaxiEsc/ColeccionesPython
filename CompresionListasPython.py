# La comprension de listas es una forma eficiente para crear listas a partir de un iterable(como lo son las listas,sets,diccionarios e iterables).
# Permiote filtrar elementos y aplicar expresiones a cada elementode un iterable de manera legible bajo una linea de codigo
# La idea de la compresion de listas se basa en esta linea de codigo.

#Sintaxis Comprension de listas
# [nueva_expresion for elemento in iterable if condicion]

#Sobre la la nueva expresion: Nos define como se modifica o procesa el elemento del iterable

#Sobre el elemento: Esta es simplente la variable del iterable original

#Iterable La secuencia o coleccion sobre donde se esta realizando la iteracion.

#Condicion: Esta es opcional para su uso es mas para el filtro del iterable

print('--> Compresion de Listas <--')

# Una lista con el cuadrado de cada numero
numeros = [1, 2, 3, 4, 5]
cuadrados = [x**2 for x in numeros] #con esto la idea es simplemente elevar al cuadrado todos los numeros de la lista en una sola linea de codigo
print(cuadrados)

# Lista de numeros pares
numeros = range(10+1)
pares = [x for x in numeros if x % 2 == 0] # Con esto se buscara devolver a quellos numeros pares de una lista del 1 al 10
print(pares)

# Lista saludando a cada nombre
nombres = ['Ana', 'Jerónimo', 'Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres] #Aqui la idea es saludar a todos las personas de esta lista
print(saludando)