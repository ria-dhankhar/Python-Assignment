# Function to check if a number is even or odd

def check_even_or_odd():

    # Prompt the user to enter a number

    number = int(input("Enter a number: "))
    
    # Check if the number is even or odd

    if number % 2 == 0:
        print("The number", number, "is even.")

    else:
        print("The number", number, "is odd.")

# Call the function to execute the program

check_even_or_odd()































