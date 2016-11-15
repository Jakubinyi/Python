import random

i = 1

print("\nKő-papír-olló ")
print("\nVálassz egyet! ")

def hand():
    if hand2 == "Kő" or hand2 == "kő":
        hand2 = 1
    elif hand2 == "Papír" or hand2 == "papír":
        hand2 = 2
    elif hand2 == "Olló" or hand2 == "olló":
        hand2 = 3

def result(option1,option2):
    



while True:
    i = 1
    print("\nÚj játék, 3 menet! ")
    while i < 4:
        hand1 = random.randrange(1, 3)
        hand2 = input("{}. Menet:".format(i))