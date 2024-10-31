import requests

def buscar_equipo_por_nombre():
    equipo = input("Ingrese el nombre del equipo: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={equipo}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'teams' in data:
            for team in data['teams']:
                print(f"Nombre del equipo: {team['strTeam']}")
                print(f"Nombre alternativo: {team['strTeamAlternate']}")
                print(f"Liga: {team['strLeague']}")
                print(f"Liga 2: {team['strLeague2']}")
                print(f"Liga 3: {team['strLeague3']}")
                print(f"Liga 4: {team['strLeague4']}")
                print(f"Estadio: {team['strStadium']}")
                print(f"Ubicación: {team['strLocation']}")
                print(f"Apodo: {team['strKeywords']}")
        else:
            print("No se encontraron resultados para ese equipo.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def buscar_equipo_por_deporte():
    deporte = input("Ingrese el nombre del deporte: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php&s={deporte}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if 'teams' in data:
            for team in data['teams']:
                print(f"Nombre del equipo: {team['strTeam']}")
                print(f"Deporte: {team['strSport']}")
                # Puedes agregar aquí los demás campos que necesites
        else:
            print("No se encontraron equipos para ese deporte.")
    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

def mostrar_menu():
    print("Menú de búsqueda:")
    print("1. Buscar por nombre de equipo")
    print("2. Buscar por deporte")
    opcion = input("Ingrese la opción deseada (o 'salir' para terminar): ")
    
    if opcion.lower() == "salir":
        return  # Sale de la función

    if opcion == "1":
        buscar_equipo_por_nombre()
    elif opcion == "2":
        buscar_equipo_por_deporte()
    else:
        print("Opción inválida.")

if __name__ == "__main__":
    while True:
        mostrar_menu()