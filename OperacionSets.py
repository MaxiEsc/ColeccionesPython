#Estas son algunas de las operaciones destacadas que se pueden realizar con los sets

print('--> Operaciones con Set <--')

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

#Union lo que permite la union de ambos sets sin repeticiones.
union = a | b
print(f'Union a | b: {union}')

#Permite agarrar solo los elementos en comun
interseccion = a & b
print(f'Intersección a & b {interseccion}')

#Son los elementos que se eliminan del conjunto a menos el b
diferencia = a - b
print(f'Diferencia a - b {diferencia}')