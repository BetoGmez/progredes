import requests
import json

def buscar_equipo():
    equipo = input("Ingrese el nombre del equipo: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t={equipo}"
    response = requests.get(url)
    storage = response.json()

    if 'teams' in storage and storage['teams']:
        for team in storage['teams']:
            nombre = team.get("strTeam", "No disponible")
            liga = team.get("strLeague", "No disponible")
            descripcion = team.get("strDescriptionES", "No disponible")
            pagina_oficial = team.get("strWebsite", "No disponible")
            estadio = team.get("strStadium", "No disponible")
            print(f"Nombre: {nombre}")
            print(f"Nombre de la Liga: {liga}")
            print(f"Descripción: {descripcion}")
            print(f"Pág. Oficial: {pagina_oficial}")
            print(f"Estadio: {estadio}")
    else:
        print("No se encontró el equipo.")

def buscar_jugador():
    jugador = input("Ingrese el nombre del jugador: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?p={jugador}"
    response = requests.get(url)
    storage = response.json()

    if 'player' in storage and storage['player']:
        for player in storage['player']:
            nombre_completo = player.get("strPlayer", "No disponible")
            nacionalidad = player.get("strNationality", "No disponible")
            equipo = player.get("strTeam", "No disponible")
            lugar_nacimiento = player.get("strBirthLocation", "No disponible")
            facebook = player.get("strFacebook", "No disponible")
            altura = player.get("strHeight", "No disponible")
            peso = player.get("strWeight", "No disponible")
            print(f"Nombre completo: {nombre_completo}")
            print(f"Nacionalidad: {nacionalidad}")
            print(f"Equipo: {equipo}")
            print(f"Lugar de nacimiento: {lugar_nacimiento}")
            print(f"Facebook: {facebook}")
            print(f"Altura: {altura}")
            print(f"Peso: {peso}")
    else:
        print("No se encontró el jugador.")

def buscar_ligas():
    url = "https://www.thesportsdb.com/api/v1/json/3/all_leagues.php"
    response = requests.get(url)
    storage = response.json()

    if 'leagues' in storage and storage['leagues']:
        for league in storage['leagues']:
            id_liga = league.get("idLeague", "No disponible")
            nombre_liga = league.get("strLeague", "No disponible")
            print(f"ID de la liga: {id_liga}, Nombre de la liga: {nombre_liga}")
    else:
        print("No se encontraron ligas.")

def buscar_liga_por_id():
    liga_id = input("Ingrese el ID de la liga: ")
    url = f"https://www.thesportsdb.com/api/v1/json/3/lookupleague.php?id={liga_id}"
    response = requests.get(url)
    storage = response.json()

    if 'leagues' in storage and storage['leagues']:
        for league in storage['leagues']:
            nombre_liga = league.get("strLeague", "No disponible")
            descripcion = league.get("strDescriptionEN", "No disponible")
            pais = league.get("strCountry", "No disponible")
            año_fundacion = league.get("intFormedYear", "No disponible")
            print(f"Nombre de la liga: {nombre_liga}")
            print(f"Descripción: {descripcion}")
            print(f"País: {pais}")
            print(f"Año de fundación: {año_fundacion}")
    else:
        print("No se encontró la liga.")

def menu():
    while True:
        print("Seleccione una opción:")
        print("1. Buscar equipo")
        print("2. Buscar jugador")
        print("3. Buscar ligas")
        print("4. Buscar liga por ID")
        print("5. Salir")

        opcion = input("Ingrese su opción: ")

        if opcion == '1':
            buscar_equipo()
        elif opcion == '2':
            buscar_jugador()
        elif opcion == '3':
            buscar_ligas()
        elif opcion == '4':
            buscar_liga_por_id()
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
