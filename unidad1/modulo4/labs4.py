# 4.3.1.6 LABORATORIO: Un año bisiesto: escribiendo tus propias funciones
''' Nombre: Luis Alberto Romero Gómez
    Descripcion: Usar las propias funciones
    Fecha: 01 de octubre'''
'''
def is_year_leap(year):
  Determina si un año es bisiesto.

  Args:
    year: El año a evaluar.

  Returns:
    True si el año es bisiesto, False en caso contrario.
  

  if year % 4 == 0:
    if year % 100 == 0:
      return year % 400 == 0
    else:
      return True
  else:
    return False

# Código de prueba
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
  yr = test_data[i]
  print(yr,"->",end="")
  result = is_year_leap(yr)
  if result == test_results[i]:
    print("OK")
  else:
    print("Fallido")
    '''

#4.3.1.7 LABORATORIO: ¿Cuántos días?: escribiendo y utilizando tus propias funciones
