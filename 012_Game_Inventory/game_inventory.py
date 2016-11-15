inv = {"rope": 1, "torch": 6, "gold_coin": 42, "dagger": 1, "arrow": 12}
dragon_loot = ["gold_coin", "dagger", "gold_coin", "gold_coin", "ruby"]

# Step 1: Write a function named display_inventory() that would take any
# possible “inventory” and display it.


def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for key, value in inventory.items():
        print("{} {}" .format(value, key))    # print("%d %s" % (value, key))
        total += value
    # print("Total number of items: %d" % (total))
    print("Total number of items: {}" .format(total))

# Step 2: Write a function named add_to_inventory(inventory, added_items), where the inventory parameter is a
# dictionary representing the player’s inventory and the added_items parameter is a list like dragon_loot.
# The add_to_inventory() function should return a dictionary that represents the updated inventory.
# Note that the added_items list can contain multiples of the same item.


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            # inventory.update({item: inventory.get(item, 0) + 1})
            inventory[item] = 1

# Step 3: Write a function named print_table(order) that takes your inventory and displays it in a well-organized table with each column right-justified.
# The input argument is an order parameter (string), which works as the following:
# - empty (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) in descending order
# - "count,asc" means the table is ordered by count in ascending order


def print_table(order):
    longest_length = len(max(inv, key=len))

    print("Inventory:")
    print("{0:>{width}s}   {1:>{width}s}".format(
        "count", "item name", width=longest_length))

    dashline_lenght = longest_length * 2 + 3

    print_dashline(dashline_lenght)

    inv_list = [(key, value) for key, value in inv.items()]

    if len(order) == 0:
        for i, j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(
                j, i, width=longest_length))

    elif order[0] == "count,asc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1])

        for i, j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(
                j, i, width=longest_length))

    elif order[0] == "count,desc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1], reverse=True)

        for i, j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(
                j, i, width=longest_length))

    else:
        print("invalid arg for print_table()")
        exit()

    print_dashline(dashline_lenght)

    print("Total number of items: {}" .format(total_number(inv)))


def print_dashline(lenght):
    for i in range(lenght):
        print("-", end="")
    print("\n")


def total_number(inventory):
    total = 0
    for value in inventory.values():
        total += value
    return total

# EXPORT


def export_inventory(filename):
    ftext = ""
    for element in inventory:
        # print str(element) + " " + str(inventory[element])
        ftext += str(element) + "," + str(inventory[element]) + "\n"

    if filename == "":
        filename = "export_inventory.csv"

    file_ = open(filename, "w+")
    file_.write(ftext)
    file_.close()

# IMPORT


def import_inventory(filename):
    if filename == "":
        filename = "import_inventory.csv"

    file_ = open(filename, "r+")
    for line in file_:
        line = line.strip()

        current_data = ""
        datas = []
        for char in line:
            if not char == ",":
                current_data += char
            else:
                datas.append(current_data)
                current_data = ""
        datas.append(current_data)

        inventory[datas[0]] = int(datas[1])


# Test:
# add_to_inventory(inv, dragon_loot)
order = ["count,asc"]
print_table(order)
