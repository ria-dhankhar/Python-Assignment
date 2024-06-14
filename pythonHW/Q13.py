# Q) Write a program that asks the user for their birth year and calculates their age

def calculate_age():

    # Prompt the user to enter their birth year
    birth_year = int(input("Enter your birth year: "))
    
    # Get the current year
    current_year = 2024
    
    # Calculate the age
    age = current_year - birth_year
    
    # Print the age
    print("Your age is:", age)

# Call the function to execute the program
calculate_age()























