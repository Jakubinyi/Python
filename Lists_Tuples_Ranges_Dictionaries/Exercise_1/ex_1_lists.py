a = [1, 3, 5]
b = [2, 4, 6]

c = a + b
print(c)

d = list(c)
d.sort()  # d = sorted(c)

print(d)
print(c)

d.reverse()
print(d)

c[3] = 42
print(c)

d.append(10)
print(d)

c.extend([7, 8, 9])
print(c)

print(c[0:3])

print(d[-1])

print(len(d))