"""1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero."""


def divide_numbers():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))

        result = num1 / num2
        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    except ValueError:
        print("Error: Please enter valid numbers!")

divide_numbers()

#------------------------------------------------------------------

"""2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer."""

def get_integer():
    user_input = input("Enter an integer: ")

    try:
        number = int(user_input)
        print("You entered:", number)

    except ValueError:
        raise ValueError("Invalid input! Please enter a valid integer.")

get_integer()

#-----------------------------------------------------------------------------

"""3. Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist."""


def read_file():
    try:
        file_name = input("Enter file name: ")
        file = open(file_name, "r")

        content = file.read()
        print("File content:\n", content)

        file.close()

    except FileNotFoundError:
        print("Error: File not found!")

read_file()

#-------------------------------------------------------------------------------

"""4. Write a Python program that prompts the user to input two numbers and raises a 
TypeError exception if the inputs are not numerical"""

def check_numbers():
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:

        n1 = float(num1)
        n2 = float(num2)

        print("Both inputs are valid numbers.")
        print("Sum:", n1 + n2)

    except ValueError:
        raise TypeError("Invalid input! Both values must be numbers.")

check_numbers()

#---------------------------------------------------------------------------------

"""5. Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue."""


def open_file():
    try:
        file_name = input("Enter file name: ")

        with open(file_name, "r") as file:
            content = file.read()
            print("File content:\n", content)

    except PermissionError:
        print("Error: You do not have permission to access this file!")

    except FileNotFoundError:
        print("Error: File not found!")

open_file()

"""6. Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range."""

def access_list():
    try:
        numbers = [10, 20, 30, 40, 50]

        index = int(input("Enter index: "))
        print("Element at index:", numbers[index])

    except IndexError:
        print("Error: Index out of range!")

    except ValueError:
        print("Error: Please enter a valid integer!")

access_list()

"""7. Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error."""

def divide():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))

        result = num1 / num2
        print("Result:", result)

    except ArithmeticError:
        print("Error: Arithmetic problem occurred (like division by zero)!")

divide()