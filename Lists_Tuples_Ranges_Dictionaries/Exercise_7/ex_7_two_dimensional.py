# Create a list a which contains three tuples. 
# The first tuple should contain a single element, the second two elements and the third three elements.
a = [
    (1,),
    (2, 2),
    (3, 3, 3),
]

# Print the second element of the second element of a.
print(a[1][1])

# Create a list b which contains four lists, each of which contains four elements.
b = [
    list(range(10)),
    list(range(10, 20)),
    list(range(20, 30)),
    list(range(30, 40)),
]

# Print the last two elements of the first element of b.
print(b[0][1:-1])