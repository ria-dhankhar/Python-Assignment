# Function to read the content of a text file and print it

def read_from_file():

    # Open the file in read mode
    with open("output.txt", "r") as file:

        # Read the content of the file
        content = file.read()
    
    # Print the content to the console
    print("The content of the file is:")
    print(content)

# Call the function to execute the program
read_from_file()
















