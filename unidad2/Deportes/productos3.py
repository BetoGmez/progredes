import requests
import time 

while True:
    id = input('Ingrese la id del producto: ')
    if id == 'salir' or id == 's':
        break
    
    url = f"https://fakestoreapi.com/products/{id}"
    
    response = requests.delete(url)
    
    if response.status_code == 200:
        print(f"Producto con ID {id} eliminado correctamente.")
    else:
        print(f"Error al eliminar el producto con ID {id}.")
    
    time.sleep(2)
