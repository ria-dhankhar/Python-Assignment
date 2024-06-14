# Q) Write a python program that calculates the sum of the digits of a given number

def sum_of_digits():
    
    # Prompt the user to enter a number
    number = input("Enter a number: ")
    
    sum_digits = 0
    
    for digit in number:
        
        # Convert the digit to an integer and add it to the sum
        sum_digits += int(digit)
    
    # Print the sum of the digits
    print("The sum of the digits is:", sum_digits)

# Call the function to execute the program
sum_of_digits()


















