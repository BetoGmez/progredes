import requests
import time 

while True:
    id = input('Ingrese la id del producto: ')
    if id == 'salir' or id == 's':
        break
    
    url = f"https://fakestoreapi.com/products/{id}"
    
    productos = requests.get(url).json()
    print(productos)
    time.sleep(2)