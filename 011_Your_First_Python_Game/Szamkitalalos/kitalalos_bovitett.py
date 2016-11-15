import random

i = 1

while True:
    num1 = random.randrange(1, 101)
    print("\nGondoltam egy számra 1 és 100 között, 8 tipp-ből találd ki! \nX-re kilép! \n")

    while i < 9:
        while True:
            num2 = input("{}. Tipp:".format(i))
            if num2.isdigit():
                num2 = int(num2)
                break
            elif num2 == "X" or num2 == "x":
                print("Kilépés")
                exit()  
            else:
                print("Számot írj be!")
        
        if num2 == num1:
            print("Talált! :) \n")
            new = input("Még egy játék? [Y/N]:")
            if new == "y" or new == "Y":
                i = 1
                break
            else:
                print("Kilépés")
                exit() 
        
        elif num2 < num1:
            print("Nagyobbra gondoltam!")
            i +=1

        elif num2 > num1:
            if num2 >100:
                print("Jóval kisebbre gondoltam!!! ")
            else:
                print("Kisebbre gondoltam!")
                i +=1

        if i == 9:
            print("\nVesztettél :( \n")
            new = input("Még egy játék? [Y/N]:")
            if new == "y" or new == "Y":
                i = 1
                break
            else:
                print("Kilépés")
                exit()  
