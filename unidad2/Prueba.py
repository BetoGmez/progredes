import requests

def obtener_datos_show(nombre):
    url = f"https://api.tvmaze.com/search/shows?q={nombre}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        if datos:
            show = datos[0]['show']  # Tomamos el primer resultado
            return {
                "nombre": show.get("name", "No disponible"),
                "resumen": show.get("summary", "No disponible"),
                "genero": show.get("genres", ["No disponible"]),
                "pais": show.get("network", {}).get("country", {}).get("name", "No disponible")
            }
    return None

def mostrar_datos(datos):
    print("\nInformación del programa:")
    print(f"Nombre: {datos['nombre']}")
    print(f"Resumen: {datos['resumen']}")
    print(f"Géneros: {', '.join(datos['genero'])}")
    print(f"País: {datos['pais']}")

def buscar_por_nombre():
    nombre = input("Ingrese el nombre del programa: ").strip()
    if nombre:
        datos = obtener_datos_show(nombre)
        if datos:
            mostrar_datos(datos)
        else:
            print("No se encontró el programa.")
    else:
        print("El nombre no puede estar vacío.")

def buscar_por_genero():
    genero = input("Ingrese el género del programa: ").strip()
    if genero:
        url = f"https://api.tvmaze.com/search/shows?q={genero}"
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos:
                print("\nProgramas encontrados:")
                for show in datos:
                    if genero.capitalize() in show['show'].get("genres", []):
                        print(f"- {show['show']['name']}")
            else:
                print("No se encontraron programas de ese género.")
        else:
            print("Error en la consulta a la API.")
    else:
        print("El género no puede estar vacío.")

def menu():
    while True:
        print("\nMenú:")
        print("1. Buscar por nombre ('Breaking Bad')")
        print("2. Buscar por género ('Drama')")
        print("3. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            buscar_por_nombre()
        elif opcion == "2":
            buscar_por_genero()
        elif opcion == "3":
            print("Adios")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

# Ejecutamos el menú
menu()
