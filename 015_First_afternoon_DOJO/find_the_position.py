import string


def position(alphabet):
    index = string.ascii_lowercase.index(alphabet)
    return int(index) + 1

# Test
print(position("a"))
print(position("z"))
print(position("e"))
