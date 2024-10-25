import requests
import time
latitud= 19.4450
longitud=-99.1310
clave="e06e47bc8aef58bdd50efcfeba68381d"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data=requests.get(main_api).json()
#print(json_data)

codigo = json_data['cod']

while True:
    latitud=input("Ingresa la latitud: ")
    longitud=input("Ingresa la longitud: ")
    main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
    json_data=requests.get(main_api).json()
    codigo = json_data['cod']

    if codigo==200:
        print(f"El codigo {codigo} indica que la respuesta es correcta")
    else:
        print(f"El codigo {codigo} indica que la respuesta es incorrecta")
    time.sleep(3)