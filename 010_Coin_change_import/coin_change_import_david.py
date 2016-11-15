o = open("money.txt", "r")

money = []

for i in o:
    money.append(i.strip())

print("Money: ", money)

for num in money:

    ten = 0
    five = 0
    two = 0
    one = 0

    rest = int(num)

    if rest >= 10:
        ten = rest // 10
        rest = rest % 10
    if rest >= 5:
        five = rest // 5
        rest = rest % 5
    if rest >= 2:
        two = rest // 2
        rest = rest % 2
    if rest >= 1:
        one = rest // 1
        rest = rest % 1
    
    print("The money is: ", num)
    print("It is:\n", ten, "piece(s) of 10\n", five, "piece(s) of 5\n", two, "piece(s) of 2\n", one, "piece(s) of 1\n")