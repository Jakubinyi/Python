import random
import time
attList = [0] * 3
defList = [0] * 3
attLosses = 0
defLosses = 0
attRolls = input('Enter the number of attack rolls: ')
while True:
    try:
        attRolls = int(attRolls)
    except ValueError:
        print('%s is not a number!' % attRolls)
        time.sleep(1)
        attRolls = input('Enter the number of attack rolls: ')
    else:
        break
while attRolls > 3:
    print('Cannot be higher than 3!')
    time.sleep(1)
    attRolls = int(input('Enter the number of attack rolls again:  '))
defRolls = input('Enter the number of defense rolls: ')
while True:
    try:
        defRolls = int(defRolls)
    except ValueError:
        print('%s is not a number!' % defRolls)
        time.sleep(1)
        defRolls = input('Enter the number of attack rolls: ')
    else:
        break
while defRolls > 3:
    print('Cannot be higher than 3!')
    time.sleep(1)
    defRolls = int(input('Enter the number of defense rolls again:  '))
print('Attacker:')
for x in range (0, attRolls):
    if x == 0:
        roll = random.randrange(1,7)
        attList[0] = roll
        print(roll, end = ' ')
    elif x == 1:
        roll = random.randrange(1,7)
        attList[1] = roll
        print(roll, end = ' ')
    elif x == 2:
        roll = random.randrange(1,7)
        attList[2] = roll
        print(roll, end = ' ')
list.sort(attList)
print('\n')
print('Defender:')
for x in range (0, defRolls):
    if x == 0:
        roll = random.randrange(1,7)
        defList[0] = roll
        print(roll, end = ' ')
    elif x == 1:
        roll = random.randrange(1,7)
        defList[1] = roll
        print(roll, end = ' ')
    elif x == 2:
        roll = random.randrange(1,7)
        defList[2] = roll
        print(roll, end = ' ')
list.sort(defList)
print('\n')
print('Results:')
if attList[2] > defList[2] and attList[2] != 0:
    defLosses = defLosses -1
elif attList[2] <= defList[2] and attList[2] != 0:
    attLosses = attLosses -1
if attList[1] > defList[1] and attList[1] != 0:
    defLosses = defLosses -1
elif attList[1] <= defList[1] and attList[1] != 0:
    attLosses = attLosses -1
if attList[0] > defList[0] and attList[0] != 0:
    defLosses = defLosses - 1
elif attList[0] <= defList[0] and attList[0] != 0:
    attLosses = attLosses - 1
print('Defender loses %d units' % defLosses)
print('Attacker loses %d units' % attLosses)






