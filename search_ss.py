import json
import requests
def get_info(people_name):

    url = "https://swapi.dev/api/people/?search="+people_name+""
    response = requests.get(url=url)

    people = response.json()

    return people

print(get_info("leia"))