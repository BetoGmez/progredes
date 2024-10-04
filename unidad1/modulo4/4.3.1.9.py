# 4.3.1.9 LABORATORIO: Números primos: ¿Cómo encontrarlos?
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Usar las propias funciones
    Fecha: 01 de octubre
'''
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Código de prueba
for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()