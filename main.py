from character import personnage
from api import move, get_character, fight, eat_item, rest, cook, equip
from loguru import logger
from helper import execute, can_craft, find_consumable
from recipes import RECIPES
from consumables import CONSUMABLES

victor = personnage("Vicktau", 50, 0, 0)

data = get_character("Vicktau")

victor = personnage(data["name"], data["hp"], data["x"], data["y"])
print(victor.hp)


while True:
    data = get_character(victor.name)
    if victor.hp > 60:
        recipe = can_craft(RECIPES, data["inventory"],exclude_slot="consumable")
        print(recipe)
        if recipe:
            execute(move, victor.name, recipe["location"][0], recipe["location"][1]) 
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
        data = get_character(victor.name)
        
        consumable_recipe = can_craft(RECIPES, data["inventory"], exclude_slot="weapon")
        if consumable_recipe:
            execute(move, victor.name, consumable_recipe["location"][0], consumable_recipe["location"][1])
            execute(cook, victor.name, consumable_recipe["output"], 1)
            data = get_character(victor.name)
        
        healing = find_consumable(data["inventory"], CONSUMABLES)
        if healing:
            result = execute(eat_item, victor.name, healing["code"], 1)
            if "data" in result:
                victor.hp = result["data"]["character"]["hp"]
        else:
            result = execute(rest, victor.name)
            if "data" in result:
                victor.hp = result["data"]["character"]["hp"]
    



