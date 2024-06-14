# Q)Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input 

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Function to get temperature input and conversion choice from user
def convert_temperature():
    print("Choose conversion:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = int(input("Enter your choice (1 or 2): "))
    
    if choice == 1:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(celsius , "Celsius is equal to", fahrenheit , "Fahrenheit")
    elif choice == 2:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(fahrenheit , "Fahrenheit is equal to ", celsius , " Celsius.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

# Call the function to execute the program
convert_temperature()





























