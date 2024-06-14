# Function to check if a substring is present in a string
def check_substring():
  
    # Prompt the user to enter the main string
    main_string = input("Enter the main string: ")
    
    # Prompt the user to enter the substring to search for
    substring = input("Enter the substring to search for: ")
    
    # Check if the substring is present in the main string
    if substring in main_string:
        print(substring , "is present in ", main_string)
  
    else:
        print(substring , "is not present in ", main_string)

# Call the function to execute the program
check_substring()












