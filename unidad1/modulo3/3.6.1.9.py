#3.6.1.9 LABORATORIO: Operando con listas - conceptos básicos
''' Nombre:  Luis Alberto Romero Gómez
    Descripcion: indexar listas y el suo de in y not in
    Fecha: 26 de septiembre'''

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

aux = set()
lista = []
for num in my_list:
    if num not in aux:
        aux.add(num)
        lista.append(num)
        
print("La lista con elementos únicos:")
print(lista)
