import random

my_list = []

for i in range(0,50):
    my_list.append(random.randint(0,100))

print("List: ", my_list, "\n")

min = my_list[0]
max = my_list[0]

for elem in my_list[0:]:
    if elem < min:
        min = elem
    if elem > max:
        max = elem

print("The min is: ", min)
print("The max is: ", max)