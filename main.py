from character import personnage
from api import move, get_character, fight, eat_item, rest, cook
from helper  import execute
from loguru import logger

victor = personnage("Vicktau", 50, 0, 0)

data = get_character("Vicktau")

victor = personnage(data["name"], data["hp"], data["x"], data["y"])
print(victor.hp)

while True:
    if victor.hp > 20:
        execute(move, victor.name, 0, 1)
        result = execute(fight, victor.name)
        if "data" in result:
            fight_result = result["data"]["fight"]["result"]
            final_hp = result["data"]["fight"]["characters"][0]["final_hp"]
            logger.info(f"Combat: {fight_result} | HP: {final_hp}")
            victor.hp = final_hp
    else:
        logger.warning("HP bas !")
        data = get_character(victor.name)
        has_food = any(slot["code"] in ["raw_chicken", "cooked_chicken"] and slot["quantity"] > 0 for slot in data["inventory"])
        if has_food:
            result = execute(move, victor.name, 1, 1)

            if any(slot["code"] == "raw_chicken" and slot["quantity"] > 0 for slot in data["inventory"]):
                result = execute(cook, victor.name, "cooked_chicken", 1)

            result = execute(eat_item, victor.name, "cooked_chicken", 1)
            if "data" in result:
                victor.hp = result["data"]["character"]["hp"]
        else:
            result = execute(rest, victor.name)
            if "data" in result:
                victor.hp = result["data"]["character"]["hp"]

    




