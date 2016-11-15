while True:
    num1 = input("Enter a number (or a letter to exit): ")
    if num1.isdigit():
        num1 = int(num1)
    else:
        print("Exit")
        exit()

    operator = input("Enter an operator : ")

    num2 = int(input("Enter another number: "))

    if operator == "+":
        ans = num1 + num2
        print("Result:", ans, "\n")
    else:
        pass

    if operator == "/":
        ans = num1 / num2
        print("Result:",ans, "\n")
    else:
        pass

    if operator == "-":
        ans = num1 - num2
        print("Result:",ans, "\n")
    else:
        pass

    if operator == "*":
        ans = num1 * num2
        print("Result:",ans, "\n")
    else:
        pass