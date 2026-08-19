while True:
    firstNum = float(input("Please enter the first number: "))
    secondNum = float(input("Please enter the second number: "))
    result = 0
    operator = input("Enter operator (+, -, *, /): ")

    while True:
        if operator not in ['+', '-', '*', '/']:
            operator = input("You entered invalid oprator, please enter operator (+, -, *, /): ")
        else:
            break

    if(operator == '+'):
        result = firstNum + secondNum
    elif(operator == '-'):
        result = firstNum - secondNum

    elif(operator == '*'):
        result = firstNum * secondNum
    elif(operator == '/'):
        if(secondNum == 0):
            print("Error: Cannot divide by zero")
            reult = None
        else:
            result = firstNum / secondNum
    if result is not None:
        print(f'Result: {result}')
    startAgain = input("Do you want to calculate again? (yes/exit): ")
    if startAgain.upper() == "EXIT":
        print("Thank You:)")
        break