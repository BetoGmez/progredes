#3.2.1.10 LABORATORIO: La sentencia continue - El Feo Devorador de Vocales
''' Nombre:  Luis Alberto Romero Gómez
    Descripcion: Uso del continue
    Fecha: 24 de septiembre'''
'''# Indicar al usuario que ingrese una palabra
user_word=input("Ingresa una palabra: ")
# y asignarlo a la variable user_word.
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A" or letter == "E":
        continue
    elif letter == "I" or letter == "O":
        continue
    elif letter == "U":
        continue
    print(letter)
'''