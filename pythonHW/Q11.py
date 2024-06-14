# Q) Write a python program that generates the first n numbers in the Fibonacci sequence

def generate_fibonacci():

    # Prompt the user to enter the value of n
    n = int(input("Enter the number of terms: "))
    
    # Initialize the first two numbers in the Fibonacci sequence
    a, b = 0, 1
    
    # Initialize an empty list to store the Fibonacci sequence
    fibonacci_sequence = []
    
    # Generate the Fibonacci sequence
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    # Print the Fibonacci sequence
    print("The first", n, "numbers in the Fibonacci sequence are:")
    print(fibonacci_sequence)

# Call the function to execute the program
generate_fibonacci()





















