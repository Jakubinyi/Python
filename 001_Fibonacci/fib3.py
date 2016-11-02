def fibonacci(n):
    a,b = 1,1
    while True:
        yield a
        a,b = b, a + b

print("Fibonacci sequance:")

n = 0
for i in fibonacci():
    if n >= 10:
        break;
    print(i)
    n += 1
