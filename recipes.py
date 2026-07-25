RECIPES = [
    {"output": "apprentice_gloves", "slot": "weapon", "ingredients": {"feather": 6}},
]


items_to_keep = []
for recipe in RECIPES:
    for ingredient in recipe["ingredients"]:
        items_to_keep.append(ingredient)

