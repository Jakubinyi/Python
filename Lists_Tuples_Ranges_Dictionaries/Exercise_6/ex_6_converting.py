# Convert a list which contains the numbers 1, 1, 2, 3 and 3, and convert it to a tuple a.
my_list = [1, 1, 2, 3, 3]
a = tuple(my_list)

# Convert a to a list b. Print its length.
b = list(a)
print(len(b))

# Convert b to a set c. Print its length.
c = set(b)
print(len(c))

# Convert c to a list d. Print its length.
d = list(c)
print(len(d))

# Create a range which starts at 1 and ends at 10. Convert it to a list e.
e = list(range(1,11))

# Create the directory dict from the previous example. 

directory = {
    "Jane Doe": "+27 555 5367",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
# ??? dict([("Jane Doe", "+27 555 5367"),("John Smith", "+27 555 6254"),("Bob Stone", "+27 555 5689")])

# Create a list t which contains all the key-value pairs from the dictionary as tuples.
t = list(directory.items())  #tuple?

# Create a list v of all the values in the dictionary.
v = list(directory.values())

# Create a list k of all the keys in he dictionary.
k = list(directory)

# Create a string s which contains the word "antidisestablishmentarianism". 
#Use the sorted function on it. What is the output type? 
#Concatenate the letters in the output to a string s2.
s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))

# Split the string "the quick brown fox jumped over the lazy dog" into a list w of individual words.
w = "the quick brown fox jumped over the lazy dog".split()