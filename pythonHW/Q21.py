# Q) Write a python program that counts the occurrences of a specific element in a list

#  Function to count occurrences of a specific element in a list
def count_occurrences(input_list, element):
    # Initialize count to 0
    count = 0
    
    # Iterate through each element in the list
    for item in input_list:
        if item == element:
            count += 1  # Increment count if the element matches
    
    # Return the count of occurrences
    return count

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

# Prompt the user to enter the element to count occurrences of
target_element = int(input("Enter the element to count occurrences of: "))

# Calculate the number of occurrences of the target_element in the list
occurrences = count_occurrences(numbers, target_element)

# Print the result
print(f"Number of occurrences of {target_element}:", occurrences)
























