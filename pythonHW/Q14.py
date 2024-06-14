# Q) Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines

def read_and_print_lines():

    # Initialize an empty list to store the lines
    lines = []
    
    print("Enter lines of text (press Enter on an empty line to finish):")
    
    while True:
        # Read a line of input from the user
        line = input()
        
        # Check if the line is empty
        if line == "":
            break
        
        # Add the line to the list
        lines.append(line)
    
    # Print all the lines entered by the user
    print("You entered:")
    for line in lines:
        print(line)

# Call the function to execute the program
read_and_print_lines()

























