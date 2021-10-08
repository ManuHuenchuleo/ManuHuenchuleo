import requests
import json


def get_people(link):
    response = requests.get(link)
    people = json.loads(response.content)
    for character in people["results"]:
        if "https://swapi.dev/api/films/4/" in character["films"]:
            yield character["name"]
    if "next" in people and people["next"] is not None:
        next_page = get_people(people["next"])
        for page in next_page:
            yield page

returnofsith = get_people("https://swapi.dev/api/people/")
for result in returnofsith:
    print(result)
