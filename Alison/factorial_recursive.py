def factorial (number):
    if number <=1:  #base case
        return 1
    else:
        return number*factorial(number-1)

user_input = eval(input("Enter a non-negative integer to take the factorial of: "))
factorial_of_user_input = factorial(user_input)
print(factorial_of_user_input)