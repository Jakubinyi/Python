def fibonacci(n):
    a,b = 1, 1
    for i in range(n-1):
        a, b = b, a + b
        return a

num = input("How many numbers do you want to print out? ")

print("Fibonacci sequance:")

for i in range (0,int(num)):
    print(int(i+1),". ", fibonacci(i))
