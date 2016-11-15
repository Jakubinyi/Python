my_file = open("money.txt", "r")
output_list = []

for line in my_file:
    output_list.append(line)    
my_file.close()

my_file = open("money.txt", "w")

for i in output_list:
    my_file.write(str(i) + "\n")