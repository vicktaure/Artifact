from character import personnage
from api import *
from loguru import logger
from helper import execute, can_craft, find_consumable, find_best_task_monsters
from recipes import RECIPES
from consumables import CONSUMABLES
import threading
import time

victor = personnage("Vicktau", 50, 0, 0,0)

data = get_character("Vicktau")

data_lumberjack = get_character("strongman")
lumberjack = personnage(data_lumberjack["name"], data_lumberjack["hp"], data_lumberjack["x"], data_lumberjack["y"], data_lumberjack["level"])

data_crafter = get_character("crafteur")
crafter = personnage(data_crafter["name"], data_crafter["hp"], data_crafter["x"], data_crafter["y"], data_crafter["level"])

victor = personnage(data["name"], data["hp"], data["x"], data["y"], data["level"])

def run_victor():
    fight_count = 0
    while True:
        data = get_character(victor.name)

        if victor.hp > 60:
            has_task = data["task"] != ""
            if not has_task:
                execute(move, victor.name, 1, 2)
                list_task = get_tasks(victor.level)
                best_task = find_best_task_monsters(list_task["data"])
                if best_task:
                    execute(accept_task, victor.name)
                    data = get_character(victor.name)

            if data["task"] != "":
                x, y = get_monster_location(data["task"])
                execute(move, victor.name, x, y)
            else:
                execute(move, victor.name, 0, 1)

            result = execute(fight, victor.name)
            fight_count += 1
            print(f"fight_count: {fight_count}")
            if fight_count >= 5:
                fight_count = 0
                execute(move, victor.name, 4, 1)
                for slot in data["inventory"]:
                    if slot["quantity"] > 1:
                        execute(deposit, victor.name, {"code": slot["code"], "quantity": slot["quantity"] - 1})
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

def run_lumberjack():
    gathering_count = 0
    while True:
        
        x, y = get_ressource_location("ash_tree")
        execute(move, lumberjack.name,x,y)
        execute(gathering,lumberjack.name)
        gathering_count += 1
        print(f"gathering_count: {gathering_count}")
        data = get_character(lumberjack.name)
        if gathering_count >= 5:
            execute(move, lumberjack.name, 4, 1)
            for slot in data["inventory"]:
                if slot["quantity"] > 1:
                    execute(deposit, lumberjack.name, {"code": slot["code"], "quantity": slot["quantity"] - 1})
            gathering_count = 0


        

def run_crafter():
    while True:
        bank = get_bank()
        recipe = can_craft(RECIPES, bank["data"],exclude_slot="consumable")
        if recipe:
            execute(move, crafter.name, 4, 1) 
            for ingredient, quantity in recipe["ingredients"].items():
                execute(withdraw, crafter.name, {"code": ingredient, "quantity": quantity})
            
            execute(move, crafter.name, recipe["location"][0], recipe["location"][1]) 
            execute(cook, crafter.name, recipe["output"], 1)
        else:
            time.sleep(30)
        


t1 = threading.Thread(target=run_victor, daemon=True)
t2 = threading.Thread(target=run_lumberjack, daemon=True)
t3 = threading.Thread(target=run_crafter, daemon=True)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()



