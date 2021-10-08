import requests

def get_ss():
    res = requests.get("https://swapi.dev/api/starships/9/")
    
    if res.status_code == 404:
        resp = 404
    else:
        resp = res.json()

    return resp


ss_data = get_ss()
if ss_data == 404:
    print("[Error 404] Datos para mostrar no hay")
else:
    print("Name: "+ss_data["name"])
    print("Model: "+ss_data["model"])
    print("manufacturer: "+ss_data["manufacturer"])