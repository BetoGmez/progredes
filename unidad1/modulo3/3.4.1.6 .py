#3.4.1.6 LABORATORIO: Lo básico de las listas
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Uso del listas y funcion .pop
    Fecha: 26 de septiembre'''
'''hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

# Paso 1: escribe una línea de código que solicite al usuario
# reemplazar el número de en medio con un número entero ingresado por el usuario.
numero = int(input("Ingrese un nuevo número: "))
hat_list[2] = numero

# Paso 2: escribe aquí una línea de código que elimine el último elemento de la lista.
hat_list.pop()

# Paso 3: escribe aquí una línea de código que imprima la longitud de la lista existente.
print("La longitud de la lista es:", len(hat_list))

print(hat_list)
'''
