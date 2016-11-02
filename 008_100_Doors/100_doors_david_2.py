doors = [0]*100

for j in range(0, 100):
    for i in range(j, 100, j + 1):
        if doors[i] == 0:
            doors[i] = 1
        else:
            doors[i] = 0

open_doors = []

for i in range(0, len(doors)):
    if doors[i] == 1:
        open_doors.append(i + 1)

print("The following doors are open: ", str(open_doors).strip("[]"))