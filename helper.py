import time

def execute(action, *args):
    result = action(*args)
    if result and "data" in result:
        time.sleep(result["data"]["cooldown"]["total_seconds"])
    else:
        time.sleep(1)
    return result

def can_craft(recipes, inventory, exclude_slot=None):
    for recipe in recipes:
        if exclude_slot and recipe["slot"] == exclude_slot:
            continue
        can_make = True
        for ingredient, quantity_needed in recipe["ingredients"].items():
            quantity_in_inventory = sum(slot["quantity"] for slot in inventory if slot["code"] == ingredient)
            if quantity_in_inventory < quantity_needed:
                can_make = False
        if can_make:
            return recipe
    return None

def find_consumable(inventory, consumables):
    for consumable in consumables:
        if any(slot["code"] == consumable["code"] and slot["quantity"] > 0 for slot in inventory):
            if "heal" in consumable:
                return consumable
    return None

def find_best_task_monsters(tasks):
    for task in tasks:
        if  task["type"] == "monsters":
            return task
    return None