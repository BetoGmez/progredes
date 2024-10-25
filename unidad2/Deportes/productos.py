import requests

url = "https://fakestoreapi.com/products"

productos = requests.get(url)

for prod in productos.json():
    print(prod['title'], '\t', prod['price'])