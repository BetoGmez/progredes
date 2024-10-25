import http.client

conn = http.client.HTTPSConnection("netflix54.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "98648cbd84msh8fe779f234a34abp15b2f5jsnf5e097357ddb",
    'x-rapidapi-host': "netflix54.p.rapidapi.com"
}   

conn.request("GET", "/season/episodes/?ids=80077209%2C80117715&offset=0&limit=25&lang=en", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))