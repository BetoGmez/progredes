import requests

latitud= 19.4450
longitud=-99.1310
clave="e06e47bc8aef58bdd50efcfeba68381d"
main_api = f"https://api.openweathermap.org/data/2.5/weather?lat={latitud}&lon={longitud}&appid={clave}"
print(main_api)

json_data=requests.get(main_api).json()
print(json_data)
print(json_data['name'])