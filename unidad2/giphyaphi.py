# python
import json
from urllib import parse, request

url = "http://api.giphy.com/v1/gifs/search"

while  True:
    search  = input('Nombre del Actor: ')
    
    if search == 'salir':
        break
    params = parse.urlencode({
    "q": search,
    "api_key": "nwpIMrRJVwWGaC9jXR2PgUWAilps0CXM",
    "limit": "5"
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
    
    print(data['data'][0]['slug'])
    #print(json.dumps(data, sort_keys=True, indent=4))

