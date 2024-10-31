import requests

def buscar_equipo_por_nombre():
    """
    Busca un equipo de deportes por su nombre en la API de TheSportsDB.

    Esta función toma el nombre del equipo como entrada, realiza una solicitud a la API
    y muestra información detallada del equipo si se encuentra.
    """
    equipo = input("Ingrese el nombre del equipo: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={equipo}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta una excepción si la solicitud falla
        data = response.json()

        if 'teams' in data:
            for team in data['teams']:
                print(f"Nombre del equipo: {team['strTeam']}")
                # ... (mostrar otros datos del equipo)
                print(f"Página web: {team['strWebsite']}")  # Agregar campo adicional
        else:
            print("No se encontraron resultados para ese equipo.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def buscar_equipo_por_deporte():
    """
    Busca equipos de deportes por el nombre del deporte en la API de TheSportsDB.

    Esta función realiza una búsqueda más general que la anterior, ya que
    devuelve todos los equipos que practican el deporte especificado.
    """
    deporte = input("Ingrese el nombre del deporte: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php&s={deporte}"

    # ... (código similar a la función anterior)

def mostrar_menu():
    """
    Muestra un menú interactivo al usuario para seleccionar el tipo de búsqueda.
    """
    while True:
        print("Menú de búsqueda:")
        print("1. Buscar por nombre de equipo")
        print("2. Buscar por deporte")
        print("3. Salir")

        opcion = input("Ingrese la opción deseada: ").lower()

        if opcion == "3":
            break

        if opcion == "1":
            buscar_equipo_por_nombre()
        elif opcion == "2":
            buscar_equipo_por_deporte()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    mostrar_menu()