from config import TOKEN, BASE_URL
import requests

def move (name, x, y):
    url = f"https://api.artifactsmmo.com/my/{name}/action/move"

    body = { "x": x, "y": y }

    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }
    
    try:
        response = requests.post(url, headers=headers, json=body)
        data = response.json()
        
        if "error" in data:
            raise Exception(data["error"]["message"])
            
        destination = data["data"]["destination"]
        cooldown = data["data"]["cooldown"]

        
        
        print(f"✅ Moved to ({destination['x']}, {destination['y']}) on {destination['name']}")
        print(f"⏳ Cooldown started: {cooldown['total_seconds']} seconds")
        return cooldown
    except Exception as e:
        print(f"❌ {e}")
    

def get_character(name):
    url = f"https://api.artifactsmmo.com/my/characters"
    headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(url, headers=headers)

    return response.json()["data"][0]

def fight(name):

    url = f"https://api.artifactsmmo.com/my/{name}/action/fight"

    payload = { "participants": ["string"] }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)

    return response.json()

def rest(name):
    url = f"https://api.artifactsmmo.com/my/{name}/action/rest"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)

    return response.json()

def eat_item(name, item, quantity):

    url = f"https://api.artifactsmmo.com/my/{name}/action/use"

    payload = {
        "code": item,
        "quantity": quantity
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

def cook(name, item, quantity):

    url = f"https://api.artifactsmmo.com/my/{name}/action/crafting"

    payload = {
        "code": item,
        "quantity": quantity
    }
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()