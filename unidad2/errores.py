try: 
    num = int(input("Ingresa tu edad: "))
    res = 1/num
    print(num)
except Exception:
    print('Hubo un error')
finally:
    print('No se sucede de todas maneras me ejecuto')