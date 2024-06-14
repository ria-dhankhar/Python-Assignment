# Q)  Write a python program that returns the minimum and maximum values in a list of numbers

# Function to find minimum and maximum values in a list of numbers
def find_min_max(numbers):
    # Check if the list is empty
    if not numbers:
        return None, None  # Return None for both min and max if list is empty
    
    # Initialize min and max to the first element of the list
    min_value = max_value = numbers[0]
    
    # Iterate through the list to find min and max values
    for num in numbers:
        if num < min_value:
            min_value = num  
        if num > max_value:
            max_value = num  
    
    # Return the minimum and maximum values found
    return min_value, max_value

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

# Find the minimum and maximum values in the list
min_val, max_val = find_min_max(numbers)

# Print the results
print("Minimum value:", min_val)
print("Maximum value:", max_val)

















