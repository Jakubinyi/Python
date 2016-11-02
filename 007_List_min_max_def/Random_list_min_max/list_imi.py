import random

my_list = []

for i in range(0,50):
    my_list.append(random.randint(0,100))

print("List: ", my_list, "\n")

max = -1
for i in my_list:
    if i > max:
        max = i

print("Max:", max)