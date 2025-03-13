#Desempaquetar Tuplas, en este ejercicio nos proponemos a desempaquetar que conceptualmente estariamos descomponiendo los datos

print('*** Desempaquetado de Tuplas ***')  # unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado: La idea conceptual de este concepto es que con la creacion de variables en orden repartir los variables de una tupla en cuestion
# Ya que las mismas como son ineditables.
id, descripcion, precio = producto

#Imprimir los valores
print(f'Tupla completa: {producto}')
# Valores independientes ya desempaquetados
print(f'Producto: id = {id}, descripcion = {descripcion}, precio = {precio}')