#OOPS assignment

"""1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.
"""

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

r = float(input("Enter radius of circle: "))

c = Circle(r)

print("Area of circle:", c.area())
print("Perimeter (Circumference) of circle:", c.perimeter())

#------------------------------------------------------------------
"""2. Write a Python program to create a person class. 
Include attributes like name, country and date of birth. Implement a method to determine the person's age."""

from datetime import datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob should be in 'YYYY-MM-DD' format

    def calculate_age(self):
        today = datetime.today()
        birth_date = datetime.strptime(self.dob, "%Y-%m-%d")

        age = today.year - birth_date.year

        # Adjust age if birthday has not occurred yet this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        return age


# Example usage
name = input("Enter name: ")
country = input("Enter country: ")
dob = input("Enter date of birth (YYYY-MM-DD): ")

p = Person(name, country, dob)

print("Name:", p.name)
print("Country:", p.country)
print("Age:", p.calculate_age())

#---------------------------------------------------------------------

"""3. Write a Python program to create a calculator class. Include methods for basic arithmetic operations."""

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        return a / b

c = Calculator()

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", c.add(num1, num2))
print("Subtraction:", c.subtract(num1, num2))
print("Multiplication:", c.multiply(num1, num2))
print("Division:", c.divide(num1, num2))

"""4. Write a Python program to create a class that represents a shape. Include methods to calculate its area and perimeter.
 Implement subclasses for different shapes like circle, triangle, and square."""

import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side



class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

c = Circle(5)
s = Square(4)
t = Triangle(6)

print("Circle -> Area:", c.area(), "Perimeter:", c.perimeter())
print("Square -> Area:", s.area(), "Perimeter:", s.perimeter())
print("Triangle -> Area:", t.area(), "Perimeter:", t.perimeter())

#---------------------------------------------------------------------------------

"""Write a Python program to create a class representing a binary search tree. 
Include methods for inserting and searching for elements in the binary tree."""





#--------------------------------------------------------------------------------------

"""6. Write a Python program to create a class representing a stack data structure.
 Include methods for pushing and popping elements.
"""





#-----------------------------------------------------------------------------------------

"""Write a Python program to create a class representing a linked list data structure. 
Include methods for displaying linked list data, inserting and deleting nodes."""
