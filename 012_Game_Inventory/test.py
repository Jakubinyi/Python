#-*-coding: utf-8-*-
inv = {"rope": 1, "torch": 6, "gold_coin": 42, "dagger": 1, "arrow": 12}
dragon_loot = ["gold_coin", "dagger", "gold_coin", "gold_coin", "ruby"]
def display_inventory(inventory):
    print("Inventory:")
    total = 0   
 
    for key, value in inventory.items():
        print("{} {}" .format(value, key))    # print("%d %s" % (value, key))
        total += value
    print("Total number of items: {}" .format(total))    # print("Total number of items: %d" % tl))
def add_to_inventory(inventory, added_items): 
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
# Test:
add_to_inventory(inv, dragon_loot)
display_inventory(inv)