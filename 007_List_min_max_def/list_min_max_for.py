list = [123, 345, 213, 678, 43, 1, 734, 300, 23, 34, 500, 456]

min = list[0]
max = list[0]

for elem in list[0:]:
    if elem < min:
        min = elem
    if elem > max:
        max = elem

print("The min is: ", min)
print("The max is: ", max)