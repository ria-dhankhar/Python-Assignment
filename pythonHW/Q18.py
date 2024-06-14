# Function to check if two strings are anagrams

def check_anagrams():

    # Prompt the user to enter the first string
    str1 = input("Enter the first string: ")
    
    # Prompt the user to enter the second string
    str2 = input("Enter the second string: ")
    
    # Remove any spaces and convert both strings to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Check if the sorted characters of both strings are equal
    if sorted(str1) == sorted(str2):
        print("The strings are anagrams.")
    else:
        print("The strings are not anagrams.")

# Call the function to execute the program
check_anagrams()
