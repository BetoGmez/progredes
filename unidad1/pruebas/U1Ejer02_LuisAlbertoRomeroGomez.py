'''
Descripción: Fundamentos de Python
Nombre: Luis Alberto Romero Gómez
Fecha: 03/10/24
'''
# Escribe la instrucción para realizar un salto de línea
print()

# Crea una lista con cuatro de tus mejores compañeros del grupo: Francisco, Pedro, Juan, Fernando
list = ["Francisco", "Pedro", "Juan", "Fernando"]

# Escribe la instrucción para desplegar el tamaño de la lista a través de la leyenda “El tamaño de la lista es”.
print("el tamaño de la lista es: ",len(list))

# Escribe la instrucción para imprimir el contenido de la lista a través de la leyenda “El contenido de la lista es ”
print("El contenido de la lista es: ", list)

# Cambiar el segundo elemento de la lista por “Joaquín”
list.insert(1, "Joaquín")

print(list)
# Agrega un elemento más a la lista con el nombre “Luis Miguel”, utiliza la instrucción: nombres.append()
list.append("Luis Miguel")

# Elimina el tercer elemento de la lista.
list.pop(2)

# Despliega la lista en orden inverso y separados con un carácter cada nombre
print(list[::-1], sep="*")