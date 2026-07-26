RECIPES = [
    {"output": "apprentice_gloves", "slot": "weapon", "ingredients": {"feather": 6}, "location": (2,1)},
    {"output": "fried_eggs", "slot": "consumable", "ingredients": {"egg": 2},"location": (1,1)},
    {"output": "cooked_chicken", "slot": "consumable", "ingredients": {"raw_chicken": 1},"location": (1,1)},
]


items_to_keep = []
for recipe in RECIPES:
    for ingredient in recipe["ingredients"]:
        items_to_keep.append(ingredient)

