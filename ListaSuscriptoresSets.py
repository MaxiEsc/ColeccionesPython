#Con este programa vamos a realizar la gestion de los suscriptores de un canal cualquiera.
#Por lo que de verificaran si el suscriptor existe, si se elimina y la verificaciones de las cuentas existen, entre otras cosas

print('--> Lista de Suscriptores <--')

#suscriptores = {} esto no es un Sets es un diccionario.
#suscriptores = set() asi se denomica un set vacio
nuevo_suscriptor = input('Proporciona un nuevo suscriptor: ')

suscriptores = {'luisa@mail.com', 'marcos@mail.com', 'elena@mail.com'}
print(f'Lista de suscriptores inicial: {suscriptores}')
suscriptores.add(nuevo_suscriptor)

# Verifica si un nuevo suscriptor ya está en la lista
nuevo_suscriptor = 'karla@mail.com'
#Con esta linea nos preguntamos si el suscriptor existe o no
if nuevo_suscriptor in suscriptores:
    print(f'El nuevo suscriptor ya está en la lista {nuevo_suscriptor}')
#Si no existe se agrega
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista {nuevo_suscriptor}')
print(f'Lista de suscriptores: {suscriptores}')

# Eliminamos un suscriptor
suscriptor_eliminar = input('Escriba el nombre del suscriptor a eliminar: ')
#El elemento elimina simplemente elimina el sets dentro del conjunto
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} ha sido eliminado de la lista')
print(f'Lista de suscriptores: {suscriptores}')

# Verificamos la cantidad total de suscriptores
print(f'Cantidad total suscriptores: {len(suscriptores)}')

# Mostramos todos los suscriptores
print(f'--- Lista de Suscriptores ---')
for suscriptor in suscriptores:
    print(f'- {suscriptor}')