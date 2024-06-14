# Q) Write a program that reads data from a CSV file and prints it to the console

import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r', newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            for row in csvreader:
                print(', '.join(row))  # Print each row as a comma-separated string
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except IOError:
        print(f"Error: Unable to read file '{file_name}'.")
    except Exception as e:
        print(f"Error: {str(e)}")

# Example usage:
file_name = 'data.csv'  # Replace with your CSV file name

read_csv_file(file_name)
