#3.4.1.13 LABORATORIO: Lo básico de las listas - Los Beatles
''' Nombre:  Luis Alberto Romero Gómez
    Descripcion: Crear y modificar listas
    Fecha: 26 de septiembre'''
'''# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append("John Lennon")
Beatles.append("Paul McCartney")
Beatles.append("George Harrison")
print("Paso 2:", Beatles)

# paso 3
nuevos_miembros = ["Stu Sutcliffe", "Pete Best"]
for miembro in nuevos_miembros:
    Beatles.append(miembro)
print("Paso 3:", Beatles)

# paso 4
a1 = Beatles.index("Stu Sutcliffe")
del Beatles[a1]

a2 = Beatles.index("Pete Best")
del Beatles[a2]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)

# probando la longitud de la lista
print("Los Fav", len(Beatles))
'''
