# Q) Write a python program that calculates the factorial of a given number

def calculate_factorial():

    # Prompt the user to enter a number

    number = int(input("Enter a number: "))
    
    # Initialize the result to 1

    factorial = 1
    
    # Use a loop to calculate the factorial

    for i in range(1, number + 1):
        factorial = factorial * i
    
    # Print the result

    print("The factorial of", number, "is", factorial)

# Call the function to execute the program

calculate_factorial()















