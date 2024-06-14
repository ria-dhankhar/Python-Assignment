# Q) Write a python program that takes a list of numbers and returns their sum 

# Function to calculate the sum of numbers in a list

def calculate_sum(numbers):
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate through each number in the list
    for num in numbers:
        total_sum += num  # Add each number to the sum
    
    # Return the total sum
    return total_sum

# Function to get a list of numbers from the user

def get_numbers_from_user():
    # Prompt the user to enter numbers, separated by spaces
    input_numbers = input("Enter numbers separated by spaces: ")
    
    # Split the input string into a list of strings
    number_strings = input_numbers.split()
    
    # Convert each string in the list to an integer
    numbers = [int(num) for num in number_strings]
    
    # Return the list of numbers
    return numbers

# Get a list of numbers from the user
numbers = get_numbers_from_user()

# Calculate the sum of the numbers in the list
result = calculate_sum(numbers)

# Print the result
print("Sum of the numbers:", result)





















