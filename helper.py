import time

def execute(action, *args):
    result = action(*args)
    if result and "data" in result:
        time.sleep(result["data"]["cooldown"]["total_seconds"])
    else:
        time.sleep(1)
    return result

def can_craft(recipes, inventory):
    for recipe in recipes:
        can_make = True
        for ingredient, quantity_needed in recipe["ingredients"].items():
            quantity_in_inventory = sum(slot["quantity"] for slot in inventory if slot["code"] == ingredient)
            if quantity_in_inventory < quantity_needed:
                can_make = False
        if can_make:
            return recipe
    
    return None