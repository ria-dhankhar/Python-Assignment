# Q) Write a program in python that counts the frequency of each character in a string

def count_character_frequency():

    user_input = input("Enter a string: ")
    
    frequency_dict = {}
    
    # Iterate over each character in the string
    for char in user_input:
        
        # If the character is already in the dictionary, increment its count
        if char in frequency_dict:
            frequency_dict[char] += 1
        
        # If the character is not in the dictionary, add it with a count of 1
        else:
            frequency_dict[char] = 1
    
    # Print the frequency of each character
    print("Character frequencies:")
    for char, frequency in frequency_dict.items():
        print(char, ":", frequency)

# Call the function to execute the program
count_character_frequency()















