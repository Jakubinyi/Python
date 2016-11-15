#-*-coding: utf-8-*-

inventory = {"rope": 12, "torch": 21,
             "gold_coin": 60, "dagger": 12, "arrow": 2}
dragon_loot = ["gold_coin", "dagger", "torch", "ruby",
               "diamond", "ruby", "gold_coin", "gold_coin", "ruby"]

# DISPLAY INVENTORY


def display_inventory(inventory):
    print("Inventory")
    total = 0
    for element in inventory:
        print(str(inventory[element]) + " " + str(element))
        total += inventory[element]

    print("Total number of items: " + str(total) + "\n---")

# ADD TO INVENTORY


def add_to_inventory(inventory, added_items):
    for element in added_items:
        try:
            inventory[element] += 1
        except KeyError:
            inventory[element] = 1


def search_longest(inventory):
    length = 0
    for element in inventory:
        if length < len(str(element)):
            length = len(str(element))
    return length


def count_spaces(longest, string):
    spaces = longest - len(str(string))
    space_str = ""

    for i in range(0, spaces):
        space_str += " "
    return space_str


def total(inventory):
    total = 0
    for element in inventory:
        total += int(inventory[element])
    return str(total)


def bubble_sort(array):
    for pass_ in range(len(array) - 1, 0, -1):
        for i in range(pass_):
            if array[i] > array[i + 1]:
                less = array[i + 1]
                more = array[i]
                array[i] = less
                array[i + 1] = more
    return array


# PRINT TABLE
def print_table(order):

    longest = search_longest(inventory)

    nums = []
    for element in inventory:
        nums.append(inventory[element])
    longest_num = search_longest(nums)

    if not order == "":
        if order == "count,asc":
            nums = bubble_sort(nums)
        elif order == "count,desc":
            nums = bubble_sort(nums)
            nums = nums[::-1]

    # print table head
    space_str1 = count_spaces(longest_num, "count")
    space_str2 = count_spaces(longest, "item name")
    print(str(space_str1) + str("count") +
          "   " + space_str2 + str("item name"))
    print("-----------------")

    # print table rows in order
    used = []
    for number in nums:
        if not number in used:
            for element in inventory:
                if inventory[element] == number:
                    space_strn = count_spaces(longest_num, inventory[element])
                    space_str = count_spaces(longest, element)

                    print(str(space_strn) +
                          str(inventory[element]) + "   " + space_str + str(element))
        used.append(number)

    print("---\nTotal number of items: " + str(total(inventory)))


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


# COMMENTED TESTS:

# export_inventory("")

import_inventory("")


# display_inventory(inventory)
# add_to_inventory(inventory, dragon_loot)
# display_inventory(inventory)


print_table("count,desc")
