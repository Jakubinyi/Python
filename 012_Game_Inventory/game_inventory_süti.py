inv= {"rope": 12, "torch": 21, "gold_coin": 60, "dagger": 12, "arrow": 2}
dragon_loot = ["gold_coin", "dagger", "torch", "ruby", "diamond", "ruby", "gold_coin", "gold_coin", "ruby"]

#DISPLAY INVENTORY
def display_inventory(inventory):
	print ("Inventory")
	total = 0
	for element in inventory:
		print (str(inventory[element]) + " " + str(element))
		total += inventory[element]
		
	print ("Total number of items: " + str(total) + "\n---")

#ADD TO INVENTORY
def add_to_inventory(inventory, added_items):
	for element in added_items:
		try:
			inventory[element] += 1
		except KeyError:
			inventory[element] = 1

inv = add_to_inventory(inv, dragon_loot)
display_inventory(inv)