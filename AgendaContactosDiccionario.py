# Agenda de Contactos, con la estructura es posible crear un diccionario dentro de otro diccionario.

print('--> Agenda de Contactos <--')

agenda = {
    'Carlos': {
        'telefono': '55667711',
        'email': 'carlos@mail.com',
        'direccion': 'Calle Principal 132'
    },
    'María': {
        'telefono': '99887733',
        'email': 'maria@mail.com',
        'direccion': 'Avenida Central 456'
    },
    'Pedro': {
        'telefono': '55139078',
        'email': 'pedro@mail.com',
        'direccion': 'Plaza Mayor 789'
    }
}

print(agenda)

# Como acceder a la informacion de un contacto en especifico,  hay dos formad de acceder con [][] o con .get()
print(f'''Información del contacto de María:
    Teléfono: {agenda['María']['telefono']} 
    Email: {agenda.get('María').get('email')}
    Dirección: {agenda.get('María').get('direccion')}''')

# Agregar un nuevo contacto recordar que si cierto elemento no existia se agrega de una
agenda['Ana'] = {
    'telefono': '55678392',
    'email': 'ana@mail.com',
    'direccion':'Calle Salvador Diaz 321'
}

print(agenda)

# Eliminar un contacto existente, simplemeten con la funcion .pop con la llave del diccionario
agenda.pop('Pedro')
#del agenda['Pedro']
print(agenda)

# Mostramos los contactos de la agenda,  con esto simplemente se usa un ciclo for con tupla mas los items de las agenda que en si es otro diccionario.
print('\nContactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
    Email: {detalles.get('email')}
    Dirección: {detalles.get('direccion')}
''')