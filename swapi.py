import json
import requests
def get_planet(planet_id):

    url = "https://swapi.dev/api/planets/"+planet_id+"/"
    response = requests.get(url=url)

    planet = json.loads(response.text)

    #planet_name = planet["name"]
    return planet["name"]

print(get_planet("2"))
#url = "https://swapi.dev/api/planets/4/"

#response = requests.get(url=url)

#planet = json.loads(response.text)

#planet_name = planet["name"]
#print(planet_name)