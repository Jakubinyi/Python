my_file = open("file_hand.txt", "w") # létrehoz file
input_list = [ 4, 6, 8, 11]

output_list = []

for i in input_list:
    my_file.write(str(i) + "\n")   #beleír a file-ba az imput_list-et

my_file.close()  #mindig bezár a memória miatt

my_file = open("file_hand.txt", "r")

for i in my_file:
    output_list.append(i)

my_file.close()

print(output_list)

# lista kiirat


my_file = open("file_hand.txt", "r")

for line in my_file:
    print(str(line) , end="")  #end a két kiiratás mivel legyen elválasztva, mert alapbol ott a \n, így felülírja

#strip levesz \n, ha beirjuk ????megoldani, de hogy?

for i in output_list:
    i = i.strip("\n")

print(output_list)
