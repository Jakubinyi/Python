my_file = open("money.txt", "r")

my_list = [] 

for line in my_file:
    my_list.append(line.strip())  

print("Money: {}\n".format(my_list))   

for i in my_list:

    num = int(i)

    print("The money is: {}".format(num))

    ten = num // 10
    remain = num % 10
    print("Tizesek: {}".format(ten))

    five = remain // 5
    remain = remain % 5
    print("Ötösök: {}".format(five))

    two = remain // 2
    remain = remain % 2
    print("Kettesek: {}".format(two))

    one = remain // 1
    remain = remain % 1
    print("Egyesek: {}\n".format(one))