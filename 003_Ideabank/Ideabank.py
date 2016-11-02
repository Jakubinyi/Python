name_of_file = raw_input("What is the name of the file: ")
completeName = name_of_file + ".txt"
#Alter this line in any shape or form it is up to you.
file1 = open(completeName , "w")

toFile = raw_input("Write what you want into the field")

file1.write(toFile)

file1.close()