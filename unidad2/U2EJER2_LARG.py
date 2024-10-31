import json
import requests

def get_video_info(api_url, search_term, search_by="title"):
    """
    Busca un video en la API de Scorebat por título o competición y muestra toda su información.

    Args:
        api_url (str): La URL base de la API de Scorebat.
        search_term (str): El término a buscar (título o competición).
        search_by (str): El campo por el que buscar (title o competition).
    """

    try:
        # Realiza una solicitud GET a la API de Scorebat
        response = requests.get(api_url)
        # Verifica si hubo algún error en la solicitud
        response.raise_for_status()
        # Convierte la respuesta JSON a un diccionario de Python
        data = response.json()

        if "response" in data:
            # Itera sobre cada resultado de la búsqueda
            for match in data["response"]:
                # Compara el término de búsqueda con el campo especificado
                if match[search_by] == search_term:
                    print("Información del video:")
                    # Imprime cada par clave-valor del video encontrado
                    for key, value in match.items():
                        print(f"{key}: {value}")
                    return  # Termina la función al encontrar el primer resultado
        else:
            print("Estructura de la respuesta inesperada.")

    except requests.exceptions.RequestException as e:
        print(f"Error al obtener datos de la API de Scorebat: {e}")

if __name__ == "__main__":
    # Configura la URL base de la API con tu token
    api_token = "[MTg0MDg2XzE3MzAzMzkzNTJfNzdmOGZjODQ4MzkyZDc3YzkyOTAyNTc4MzRkMzdlOWVmNzQ0ZjYyZg==]"  # Reemplaza con tu token real
    main_api = f"https://www.scorebat.com/video-api/v3/feed/?token={api_token}"

    # Bucle principal del programa
    while True:
        # Muestra el menú de opciones
        print("Menú:")
        print("1. Buscar por nombre de video")
        print("2. Buscar por competición")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        # Ejecuta la acción correspondiente a la opción seleccionada
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