number = int(input("Enter a number: "))
fizzbuzz = ""
if(number % 3 == 0):
    fizzbuzz += "fizz"
if(number % 5 == 0):
    fizzbuzz += "buzz"
print(fizzbuzz)