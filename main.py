from character import personnage
from api import move, get_character, fight, eat_item, rest, cook
import time

victor = personnage("Vicktau", 50, 0, 0)

data = get_character("Vicktau")

victor = personnage(data["name"], data["hp"], data["x"], data["y"])
print(victor.hp)

while True:
    if victor.hp > 20:
        cooldown = move(victor.name, 0, 1)
        if cooldown:
            time.sleep(cooldown["total_seconds"])

        result = fight(victor.name)
        print(result)
        victor.hp = result["data"]["fight"]["characters"][0]["final_hp"]
        time.sleep(60)
    else:
        data = get_character(victor.name)
        has_food = any(slot["code"] in ["raw_chicken", "cooked_chicken"] and slot["quantity"] > 0 for slot in data["inventory"])
        if has_food:
            if cooldown:
                time.sleep(cooldown["total_seconds"])
                cooldown = cook(victor.name, "cooked_chicken", 1)
            if cooldown:
                time.sleep(cooldown["total_seconds"])
                print(cooldown)
                cooldown = eat_item(victor.name, "cooked_chicken", 1)
            if cooldown:
                    time.sleep(cooldown["total_seconds"])
        else:
            rest(victor.name)

    




