import random

my_list = []

for i in range(0,50):
    my_list.append(random.randint(0,100))

print("List: ", my_list, "\n")

min = 101
max = -1

for i in my_list:
    if i > max:
        max = i
    if i < min:
        min = i

print("Max:", max)
print("Min:", min)