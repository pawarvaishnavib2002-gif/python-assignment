#Assignment on Functions

"""1. Write a Python function to find the maximum of three numbers."""

def max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print(max(10, 25, 15))

#---------------------------------------------

"""2. Write a Python function to sum all the numbers in a list.
	Sample List : (8, 2, 3, 0, 7)
	Expected Output : 20"""

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
nums = (8, 2, 3, 0, 7)
print(sum_list(nums))

"""3. Write a Python function to multiply all the numbers in a list.
	Sample List : (8, 2, 3, -1, 7)
	Expected Output : -336"""

def list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product
nums = (8, 2, 3, -1, 7)
print(list(nums))

"""4. Write a Python function to reverse a string. 
	Sample String : "1234abcd"
	Expected Output : "dcba4321"
	"""

def reverse_string(s):
    return s[::-1]
text = "1234abcd"
print(reverse_string(text))

"""5. Write a Python function to check whether a number falls within a given range.
"""

def check_range(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False
print(check_range(5, 1, 10))

#---------------------------------------------------

"""
6. Write a Python function that accepts a string and counts the number of upper and lower case letters.
	Sample String : 'The quick Brow Fox'
	Expected Output :
	No. of Upper case characters : 3
	No. of Lower case Characters : 12"""


#-----------------------------------------------

"""7. Write a Python function that takes a list and returns a new list with distinct elements from the first list.
	Sample List : [1,2,3,3,3,3,4,5]
	Unique List : [1, 2, 3, 4, 5]
	"""

def list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = [1, 2, 3, 3, 3, 3, 4, 5]
print(list(lst))

"""8. Write a Python function that checks whether a passed string is a palindrome or not.
Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g.,
 madam or nurses run."""


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("nurses run"))

"""9. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

	Sample Items : green-red-yellow-black-white
	Expected Result : black-green-red-white-yellow"""

def sort_words(s):
    words = s.split('-')
    words.sort()
    return '-'.join(words)
text = "green-red-yellow-black-white"
print(sort_words(text))

"""10. Write a Python program to detect the number of local variables declared in a function.
"""
def sample_function():
    a = 10
    b = 20
    c = a + b
    print("Number of local variables:", len(locals()))
sample_function()

"""11. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, also create a lambda function that multiplies argument x with argument y and prints the result.

	Sample Output:
	25
	48"""

add_15 = lambda x: x + 15
multiply = lambda x, y: x * y
print(add_15(10))
print(multiply(6, 8))

"""12. Write a Python program to create a function that takes one argument, and that argument will be multiplied with an unknown given number.
	Sample Output:
	Double the number of 15 = 30
	Triple the number of 15 = 45
	Quadruple the number of 15 = 60
	Quintuple the number 15 = 75"""

def multiplier(n):
    return lambda x: x * n
double = multiplier(2)
triple = multiplier(3)
quadruple = multiplier(4)
quintuple = multiplier(5)
num = 15
print("Double the number of 15 =", double(num))
print("Triple the number of 15 =", triple(num))
print("Quadruple the number of 15 =", quadruple(num))
print("Quintuple the number 15 =", quintuple(num))

"""13. Write a Python program to sort a list of tuples using Lambda.
	Original list of tuples:
	[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
	Sorting the List of Tuples:
	[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]"""

data = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
result = sorted(data, key=lambda x: x[1])
print(result)

"""14. Write a Python program to sort a list of dictionaries using Lambda.

	Original list of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
	Sorting the List of dictionaries :
	[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]"""


data = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
result = sorted(data, key=lambda x: x['color'])
print(result)

"""15. Write a Python program to filter a list of integers using Lambda.
	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Even numbers from the said list:
	[2, 4, 6, 8, 10]
	Odd numbers from the said list:
	[1, 3, 5, 7, 9]	"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda x: x % 2 == 0, lst))
odd = list(filter(lambda x: x % 2 != 0, lst))
print("Even numbers:", even)
print("Odd numbers:", odd)

"""16. Write a Python program to square and cube every number in a given list of integers using Lambda.

	Original list of integers:
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	Square every number of the said list:
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	Cube every number of the said list:
	[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda x: x**2, lst))
cube = list(map(lambda x: x**3, lst))
print("Square:", square)
print("Cube:", cube)

#------------------------------------------------------
"""18. Write a Python program to find if a given string starts with a given character using Lambda.
"""
starts_with = lambda s, ch: s.startswith(ch)

print(starts_with("Python", "P"))
print(starts_with("Python", "p"))

#---------------------------------------------------
"""19. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.

	Original arrays:
	[-1, 2, -3, 5, 7, 8, 9, -10]
	Rearrange positive and negative numbers of the said array:
	[2, 5, 7, 8, 9, -10, -3, -1]"""

lst = [-1, 2, -3, 5, 7, 8, 9, -10]
result = sorted(lst, key=lambda x: (x < 0, x))
print(result)

#----------------------------------------------------

"""20. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

	Original arrays:
	[1, 2, 3, 5, 7, 8, 9, 10]
	Number of even numbers in the above array: 3
	Number of odd numbers in the above array: 5
	"""

lst = [1, 2, 3, 5, 7, 8, 9, 10]

even_count = len(list(filter(lambda x: x % 2 == 0, lst)))
odd_count = len(list(filter(lambda x: x % 2 != 0, lst)))
print("Number of even numbers in the above array:", even_count)
print("Number of odd numbers in the above array:", odd_count)

#---------------------------------------------------------------------
"""21. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

	Orginal list:
	[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
	Numbers of the above list divisible by nineteen or thirteen:
	[19, 65, 57, 39, 152, 190]
	"""

lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, lst))
print(result)

#-------------------------------------------------------------------------

"""22. Write a Python program to check whether a given string contains a capital letter, a lower case letter, a number and a minimum length using lambda.
"""

check_string = lambda s: (
    any(c.isupper() for c in s) and
    any(c.islower() for c in s) and
    any(c.isdigit() for c in s) and
    len(s) >= 8
)
text = "Python123"
if check_string(text):
    print("Valid String")
else:
    print("Invalid String")