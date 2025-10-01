try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print("The result is:", result)
except ValueError:
    print("Error: Invalid input. Please enter a number.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")