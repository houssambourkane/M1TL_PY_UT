inventory = {"pommes": 30, "bananes": 15, "oranges": 10}

def update_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity