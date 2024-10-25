import requests
import json

def buscar_serie(query, tipo):
    url = f"https://api.tvmaze.com/search/shows?q=Breaking%20Bad"
    api_key = "N0GZrtF8eTmnHNaMoFL2rPJpWl4hqMIm"
    response = requests.get(url)
    data = json.loads(response.text)
    
    if data:
        for show in data:
            if tipo == "nombre" and show["show"]["name"] == query:
                print("Nombre:", show["show"]["name"])
                print("Resumen:", show["show"]["summary"])
                print("Género:", ", ".join(show["show"]["genres"]))
                print("País:", show["show"]["network"]["country"]["name"])
                break
            elif tipo == "genero" and query in show["show"]["genres"]:
                print("Nombre:", show["show"]["name"])
                print("Género:", ", ".join(show["show"]["genres"]))
                break
            else:
                print("No se encontró la serie. Por favor intente con otros datos")
    else:
        print("Error en la búsqueda.")
if __name__ == "__main__":
    while True:
        opcion = input("1. Buscar por nombre\n2. Buscar por género\n3. Salir\n")

        if opcion == "1":
            nombre = input("Ingrese el nombre de la serie: ")
            buscar_serie(nombre, "nombre")
        elif opcion == "2":
            genero = input("Ingrese el género de la serie: ")
            buscar_serie(genero, "genero")
        elif opcion == "3":
            print("¡Adiós!")
            break
        else:
            print("Opción no valida.")
