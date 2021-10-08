import json
import requests
def get_starships(starships_id):

    url = "https://swapi.dev/api/starships/"+starships_id+"/"
    response = requests.get(url=url)
    if response.status_code == 404:
        starships = "error"
    else:
        starships = response.json()

    #starships_name = starships["name"]
    return starships

ss_data = get_starships("9")

if ss_data == "error":
    print("[Error 404] Datos para mostrar no hay - Yoda")
else:
    print("Name: "+ss_data["name"])
    print("Model: "+ss_data["model"])
    print("manufacturer: "+ss_data["manufacturer"])
