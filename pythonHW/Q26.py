# Q) Write a program in python that checks if a string starts with a given prefix or ends with a given suffix. 

# Function to check if a string starts with a given prefix
def starts_with_prefix(input_string, prefix):
    return input_string.startswith(prefix)

# Function to check if a string ends with a given suffix
def ends_with_suffix(input_string, suffix):
    return input_string.endswith(suffix)

# Function to get user input and perform checks
def check_prefix_suffix():
    input_string = input("Enter a string: ")
    prefix = input("Enter a prefix to check: ")
    suffix = input("Enter a suffix to check: ")

    starts_with = starts_with_prefix(input_string, prefix)
    ends_with = ends_with_suffix(input_string, suffix)

    if starts_with:
        print(f"The string '{input_string}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with the prefix '{prefix}'.")

    if ends_with:
        print(f"The string '{input_string}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with the suffix '{suffix}'.")

# Call the function to execute the program
check_prefix_suffix()




























