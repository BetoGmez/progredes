#3.2.1.11 LABORATORIO: La sentencia continue - El Bonito Devorador de Vocales
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Uso del continue
    Fecha: 24 de septiembre'''
'''word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word=input("Ingresa una palabra: ")
user_word = user_word.upper()
for letter in user_word:
    if letter == "A" or letter == "E" or letter == "I" or letter == "O":
        continue
    elif letter == "U":
        continue
    word_without_vowels=word_without_vowels+letter
# Imprimir la palabra asignada a word_without_vowels.
print(word_without_vowels)'''
