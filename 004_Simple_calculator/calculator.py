while True:
    while True:
        num1 = input("Enter a number (or a letter to exit): ")
        if num1.isdigit():
            num1 = int(num1)
            break
        else:
            print("Exit")
            exit()
            
    operator = input("Enter an operator: ")

    while True:
        num2 = input("Enter a number: ")
        if num2.isdigit():
            num2 = int(num2)
            break
        else:
            print("Exit")
            exit()

    if operator == "+":
        result = num1 + num2
        print("Result:", result, "\n")

    elif operator == "/":
        result = num1 / num2
        print("Result:",result, "\n")

    elif operator == "-":
        result = num1 - num2
        print("Result:",result , "\n")

    elif operator == "*":
        result = num1 * num2
        print("Result:",result, "\n")

    else:
        result = "Operator Error"
        print("Result:",result, "\n")
    
    