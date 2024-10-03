#3.2.1.3 LABORATORIO: Lo esencial del bucle while - Adivina el número secreto
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Uso del while
    Fecha: 23 de septiembre'''
'''secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

number = int(input("Introduce el numero: "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Introduce el numero: "))
print("¡Bien hecho, muggle! Eres libre ahora")'''
