my_file = open("testfile.txt", "r")
output_list = []

for i in my_file:
    output_list.append(int(i) + 100)
    
my_file.close()
my_file = open("testfile.txt", "w")

for i in output_list:
    my_file.write(str(i) + "\n")