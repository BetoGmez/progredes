# 4.3.1.8 LABORATORIO: Día del año: escribiendo y utilizando tus propias funciones
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Usar las propias funciones
    Fecha: 01 de octubre
'''
def is_year_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

def day_of_year(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    
    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    return total_days

# Código de prueba
print(day_of_year(2000, 12, 31))  # Resultado esperado: 366 (año bisiesto)