from character import personnage
from api import move, get_character, fight, eat_item, rest, cook, equip
from loguru import logger
from helper import execute, can_craft
from recipes import RECIPES

victor = personnage("Vicktau", 50, 0, 0)

data = get_character("Vicktau")

victor = personnage(data["name"], data["hp"], data["x"], data["y"])
print(victor.hp)


#result = execute(cook, victor.name, "apprentice_gloves", 1)
#print(result)
#result = execute(equip, victor.name,"apprentice_gloves", "weapon" )
#print(result)

while True:
    data = get_character(victor.name)
    if victor.hp > 60:
        recipe = can_craft(RECIPES, data["inventory"])
        print(recipe)
        if recipe:
            execute(move, victor.name, 2, 1)
            execute(cook, victor.name, recipe["output"], 1)
        else:
            execute(move, victor.name, 0, 1)
            result = execute(fight, victor.name)
            if "data" in result:
                fight_result = result["data"]["fight"]["result"]
                final_hp = result["data"]["fight"]["characters"][0]["final_hp"]
                logger.info(f"Combat: {fight_result} | HP: {final_hp}")
                victor.hp = final_hp
    elif victor.hp <= 60:
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
    



