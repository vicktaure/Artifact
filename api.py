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
        return {}

    

def get_character(name):
    url = f"https://api.artifactsmmo.com/my/characters"
    headers = {
    "Accept": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }
    response = requests.get(url, headers=headers)

    characters = response.json()["data"]
    for charac in characters:
        if charac["name"] == name:
            return charac

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

def equip(name, equipment, slot):

    url = f"https://api.artifactsmmo.com/my/{name}/action/equip"

    payload = [
        {
            "code": equipment,
            "slot": slot ,
            "quantity": 1
        }
    ]
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, json=payload, headers=headers)

    return response.json()

def sell(name, item, quantity):
    url = f"https://api.artifactsmmo.com/my/{name}/action/npc/sell"

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

def accept_task(name):
    url = f"https://api.artifactsmmo.com/my/{name}/action/task/new"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)

    return response.json()

def complete_task(name):
    url = f"https://api.artifactsmmo.com/my/{name}/action/task/complete"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)
    
    return response.json()

def cancel_task(name):
    url = f"https://api.artifactsmmo.com/my/{name}/action/task/cancel"
    headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)
    
    return response.json()

def get_tasks(character_level):
    url = "https://api.artifactsmmo.com/tasks/list"

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params={"min_level": character_level - 2, "max_level": character_level - 1})

    return response.json()

def get_monster_location(monster_code):

    url = "https://api.artifactsmmo.com/maps"

    querystring = {"content_type":"monster", "content_code": monster_code}

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring)
    result = response.json()
    print(result)

    return result["data"][0]["x"], result["data"][0]["y"]

def gathering(name):

    url = f"https://api.artifactsmmo.com/my/{name}/action/gathering"

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }

    response = requests.post(url, headers=headers)

    return response.json()

def get_ressource_location(ressource_code):

    url = "https://api.artifactsmmo.com/maps"

    querystring = {"content_type":"resource", "content_code": ressource_code}

    headers = {"Accept": "application/json"}

    response = requests.get(url, headers=headers, params=querystring)
    result = response.json()
    print(result)

    return result["data"][0]["x"], result["data"][0]["y"]