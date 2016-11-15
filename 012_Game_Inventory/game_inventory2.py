inv = {"rope": 1, "torch": 6, "gold_coin": 42, "dagger": 1, "arrow": 12}
dragon_loot = ["gold_coin", "dagger", "gold_coin", "gold_coin", "ruby"]

# Step 1: Display inventory


def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for key, value in inventory.items():
        print("{} {}" .format(value, key))
        total += value
    print("Total number of items: {}" .format(total))

# Step 2: Add to inventory


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

# Step 3: Print table


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

    elif order == "count,asc":
        inv_list = sorted(inv_list, key=lambda tup: tup[1])

        for i, j in inv_list:
            print("{0:>{width}d}   {1:>{width}s}".format(
                j, i, width=longest_length))

    elif order == "count,desc":
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


# Step 4: Import inventory


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

        if datas[1].isalpha():
            pass
        else:
            try:
                # if inv[datas[0]] >= 1:
                inv[datas[0]] += int(datas[1])
                # else:
                #inv[datas[0]] = int(datas[1])
            except KeyError:
                inv[datas[0]] = int(datas[1])
    file_.close()

# Step 5: Export inventory


def export_inventory(filename):
    ftext = ""
    for element in inv:
        ftext += str(element) + "," + str(inv[element]) + "\n"

    if filename == "":
        filename = "export_inventory.csv"

    file_ = open(filename, "w+")
    file_.write(ftext)
    file_.close()


# Test:
#add_to_inventory(inv, dragon_loot)
# print_table("")
# print_table("count,asc")
# print_table("count,desc")
import_inventory("")
# export_inventory("")
display_inventory(inv)
