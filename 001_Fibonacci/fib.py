fibonacci_cache = {}

def fibonacci(n):
   if n in fibonacci_cache:
       return fibonacci_cache[n]

   if n == 0 or n == 1:
        return n
        
   result = fibonacci(n-1) + fibonacci(n-2)
   fibonacci_cache[n] = result 
   return result

num = input("How many numbers do you want to print out? ")
num = int(num)

print("Fibonacci sequance:")

for i in range (0, num):
    linenumber = i + 1
    print("{}. {}".format(linenumber, fibonacci(i)))
