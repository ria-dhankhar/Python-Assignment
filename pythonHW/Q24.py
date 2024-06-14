# Q) Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result

def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operator"

# Function to get numbers and operator from user input
def get_input_and_calculate():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+, -, *, /): ")

    result = calculator(num1, num2, operator)
    print("Result: ", result)

# Call the function to execute the program
get_input_and_calculate()


















