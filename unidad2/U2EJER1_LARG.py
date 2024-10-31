# python
import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

def buscar_gif():
    search = input('Nombre del Actor: ')
    if search == 'salir':
        return False
    params = parse.urlencode({
        "q": search,
        "api_key": "nwpIMrRJVwWGaC9jXR2PgUWAilps0CXM",
        "limit": "5"
    })
    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    print("Descripcion: " + data['data'][0]['slug'])
    return True

while True:
    print("\nMenú:")
    print("1. Buscar GIF")
    print("2. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        continuar = buscar_gif()
        if not continuar:
            break
    elif opcion == "2":
        break
    else:
        print("Opción inválida. Por favor, elige 1 o 2.")

