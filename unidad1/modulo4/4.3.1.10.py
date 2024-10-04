# 4.3.1.10 LAB: Convirtiendo el consumo de combustible
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Usar las propias funciones
    Fecha: 01 de octubre
'''
def liters_100km_to_miles_gallon(liters):
    miles_per_100km = 100 * 1000 / 1609.344
    gallons = liters / 3.785411784
    return miles_per_100km / gallons

def miles_gallon_to_liters_100km(miles):
    km_per_mile = 1609.344 / 1000
    liters_per_100km = 3.785411784 / miles * 100 * km_per_mile
    return liters_per_100km

# Código de prueba
print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))