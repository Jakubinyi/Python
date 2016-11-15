# This is OK
print(5)
print(6.7)

# This is not OK
# print("3" + 4)

# Do you mean this...
print("3%d" % 4) # concatenate "3" and "4" to get "34"

# Or this?
print(int("3") + 4) # add 3 and 4 to get 7




# These lines will do the same thing
print("3%d" % 4)
print("3" + str(4))



# This is OK
int("3")

# This is OK
int(3.7)

# This is not OK
# int("3.7") # This is a string representation of a float, not an integer!

# We have to convert the string to a float first
int(float("3.7"))