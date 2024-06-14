# Function to write user input to a text file

def write_to_file():
    # Prompt the user to enter a string

    user_input = input("Enter a string: ")
    
    # Open a file in write mode

    with open("output.txt", "w") as file:

        # Write the user's input to the file
        file.write(user_input)
    
    # Inform the user that the string has been written to the file
    print("Your input has been written to output.txt")

# Call the function to execute the program
write_to_file()


























