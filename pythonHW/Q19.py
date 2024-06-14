import string

# Q) Write a python program that removes all punctuation from a given string

def remove_punctuation():

    # Prompt the user to enter a string
    input_string = input("Enter a string: ")
    
    # Create a translation table for removing punctuation
    translator = str.maketrans('', '', string.punctuation)
    
    # Remove punctuation from the input string
    no_punctuation_string = input_string.translate(translator)
    
    # Print the string without punctuation
    print("String without punctuation:", no_punctuation_string)

# Call the function to execute the program
remove_punctuation()
