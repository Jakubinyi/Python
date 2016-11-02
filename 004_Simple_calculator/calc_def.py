def calculator (num1, num2, operator):
    result = 0

    if operator == "+":
        result = num1 + num2
    
    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        result = num1 / num2
    return result

while True:
  while True:
     num1 = input("Enter a number (or a letter to exit): ")
     if num1.isdigit():
            num1 = int(num1)
            break
     else:
            print("Exit")
            exit()

  operator = input("Enter an operator : ")

  num2 = int(input("Enter another number: "))


  ans = calculator(num1, num2, operator)
  print("Result:", ans, "\n")

