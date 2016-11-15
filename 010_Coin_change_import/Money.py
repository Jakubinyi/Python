num = int(input("Mennyi pénz?:"))

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
print("Egyesek: {}".format(one))

