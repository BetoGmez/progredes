import json
import requests

def get_video_info(api_url, search_term, search_by="title"):
    """Busca un video en la API de Scorebat por título o competición y muestra toda su información.

    Args:
        api_url (str): La URL de la API de Scorebat.
        search_term (str): El término de búsqueda.
        search_by (str): El campo por el que buscar (title o competition).
    """

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        if "response" in data:
            for match in data["response"]:
                if match[search_by] == search_term:
                    print(f"Información del video:")
                    for key, value in match.items():
                        print(f"{key}: {value}")
                    return
        else:
            print("Estructura de la respuesta inesperada.")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API de Scorebat: {e}")

if __name__ == "__main__":
    api_token = "[MTg0MDg2XzE3MzAzMzkzNTJfNzdmOGZjODQ4MzkyZDc3YzkyOTAyNTc4MzRkMzdlOWVmNzQ0ZjYyZg==]"  # Reemplaza con tu token real
    main_api = f"https://www.scorebat.com/video-api/v3/feed/?token={api_token}"

    while True:
        print("Menú:")
        print("1. Buscar por nombre de video")
        print("2. Buscar por competición")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del video: ")
            get_video_info(main_api, nombre)
        elif opcion == "2":
            competicion = input("Ingrese el nombre de la competición: ")
            get_video_info(main_api, competicion, "competition")
        elif opcion == "3":
            break
        else:
            print("Opción inválida.")