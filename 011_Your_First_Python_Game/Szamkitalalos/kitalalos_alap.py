import random

i = 1

num1 = random.randrange(1, 101)

print("Gondoltam egy számra 1 és 100 között, 8 tipp-ből találd ki!")

while i < 9:
    num2 = int(input("{}. Tipp:".format(i)))
    
    if num2 == num1:
        print("Talált! :)")
        break

    elif num2 < num1:
        print("Nagyobbra gondoltam!")
        i +=1

    elif num2 > num1:
        print("Kisebbre gondoltam!")
        i +=1

if i == 9:
    print("Vesztettél")