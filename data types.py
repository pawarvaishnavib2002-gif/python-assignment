"""Q.1.Write a program to add two lists index-wise.Create a new list that contains the 0th index item from both the list,
   then the 1st index item, and so on till the last element.any leftover items will get added at the end of the new list.
   	Given List:

	list1 = ["M", "na", "i", "Ra"]
	list2 = ["y", "me", "s", "hul"]

	Output:

	[['M','y'], ['na', me'], ['i', 's'], ['Ra', 'hul']]"""

lst1=["M","na","i","Ra"]
lst2=["y","me","s","hul"]

result=[]

#Loop through both index wise

for i in range(len(lst1)):
    result.append([lst1[i],lst2[i]])
print(result)
#------------------------------------------------------------------------------------------------------
"""2. Write a program to add item 7000 after 6000 in the following Python List
	list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
	Output:
	[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]"""

lst1=[10,20,[300,400,[5000,6000,],500],30,40]

print(lst1)

lst1[2][2].append(7000)
print(lst1)

#-----------------------------------------------------------------------------------------------
""" 3. Suppose you are given a list of candy and another list of same size representing no of items of respective candy.
	i.e -
	candy_list = ['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
	no_of_items = [10,20,34,74,32]
	Write a program to show no. of items of each candy type.
	Output:
	Jelly Belly-10
	Kit Kat-20
	Double Bubble-34
	Milky Way-74
	Three Musketeers-32
	"""

candy_list=['Jelly Belly','Kit Kat','Double Bubble','Milky Way','Three Musketeers']
no_of_items=[10,20,34,74,32]

result=[]

for i in range(len(candy_list)):
    result.append(candy_list[i]+"-"+ str (no_of_items[i]))
print(result)

#-------------------------------------------------------------------------------------------

"""4. Running Sum on list Write a program to print a list after performing running sum on it.
	i.e:
	Input:
	list1 = [1,2,3,4,5,6]
	Output:
	[1,3,6,10,15,21]"""


lst1=[1,2,3,4,5,6]

sum = []
total = 0

for num in lst1:
    total = total + num
    sum.append(total)

print(sum)

#----------------------------------------------------------------------------------------------

"""5. You are given a list of integers. You are asked to make a list by running through elements of the list by adding all elements greater and itself.
	i.e. Say given list is [2,4,6,10,1] resultant list will be [22,20,10,23].
	For 1st element 2 ->> these are greater (4+6+10) values and 2 itself so on adding becomes 22.
	For 2nd element 4 ->> greater elements are (6, 10) and 4 itself, so on adding 20
	like wise for all other elememts.
	[2,4,6,10,1]-->[22,20,16,10,23]
	"""

lst1 = [2, 4, 6, 10, 1]

result = []

for i in range(len(lst1)):
    total = 0
    for j in range(len(lst1)):
        if lst1[j] >= lst1[i]:
            total += lst1[j]
    result.append(total)

print(result)

"""6. Find list of common unique items from two list. and show in increasing order
	Input
	num1 = [23,45,67,78,89,34]
	num2 = [34,89,55,56,39,67]
	Output:
	[34, 67, 89]"""

num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

result = list(set(num1) & set(num2))
result.sort()
print(result)

"""7. Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.
	Input:
	['1ac21', '23fg', '456', '098d','1','kls']
	Output:
	['456', '23fg', '1ac21', '1', 'kls', '098d']
	"""


#---------------------------------------------------------------------------------------------------------

"""8. Write a program that can find the max number of each row of a matrix
	Example:
	Input:
	[[1,2,3],[4,5,6],[7,8,9]]
	Output:
	[3,6,9]"""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for row in matrix:
    result.append(max(row))
print(result)

"""9. Shortlist Students for a Job role Ask user to input students record and store in tuples for each record. Then Ask user to input three things he wants in the candidate- Primary Skill, Higher Education, Year of Graduation.

	Show every students record in form of tuples if matches all required criteria.
	It is assumed that there will be only one primry skill.
	If no such candidate found, print No such candidate
	
	Input:

	Enter No of records- 2
	Enter Details of student-1
	Enter Student name- Manohar
	Enter Higher Education- B.Tech
	Enter Primary Skill- Python
	Enter Year of Graduation- 2022
	Enter Details of student-2
	Enter Student name- Ponian
	Enter Higher Education- B.Sc.
	Enter Primary Skill- C++
	Enter Year of Graduation- 2020

	Enter Job Role Requirement
	Enter Skill- Python
	Enter Higher Education- B.Tech
	Enter Year of Graduation- 2022
	Output

	('Manohar', 'B.tech', 'Python', '2022')
	"""
#___________________________________________________________________________________________

"""10. Write a program to find set of common elements in three lists using sets.

	Input : ar1 = [1, 5, 10, 20, 40, 80]
			ar2 = [6, 7, 20, 80, 100]
			ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
	Output : [80, 20]"""

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

result = list(set(ar1) & set(ar2) & set(ar3))
print(result)

#---------------------------------------------------------------------------------------

"""11. Write a program to count unique number of vowels using sets in a given string. Lowercase and upercase vowels will be taken as different.
	Input:

	Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"
	Output:

	No of unique vowels-6"""

Str1 = "hands-on data science mentorship progrAm with live classes at affordable fee only on CampusX"

vowels = set("aeiouAEIOU")

unique_vowels = set(ch for ch in Str1 if ch in vowels)

print("No of unique vowels-", len(unique_vowels))

#-------------------------------------------------------------------------------------------

"""12. Intersection of two lists. Intersection of two list means we need to take all those elements which are common to both of the initial lists and store them into another list. Only use using list-comprehension.
	Example 1:
	Input:
	lst1 = {15, 9, 10, 56, 23, 78, 5, 4, 9}
	lst2 = {9, 4, 5, 36, 47, 26, 10, 45, 87}
	
	Output:
	[9, 10, 4, 5]
	Example 2:
	
	Input:
	lst1 = {4, 9, 1, 17, 11, 26, 28, 54, 69}
	lst2 = {9, 9, 74, 21, 45, 11, 63, 28, 26}
	Output:
	[9, 11, 26, 28]"""

lst1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
lst2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

result = [x for x in lst1 if x in lst2 and x not in []]
result = list(dict.fromkeys(result))
print(result)
#----------------------------------------------------------------------------------

"""13. Convert a list of Tuples into Dictionary.
	Example 1:
	Input:
	[("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
	Output:
	{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}
	
	Example 2:
	Input:
	[('A', 1), ('B', 2), ('C', 3)]
	
	Output:
	{'A': [1], 'B': [2], 'C': [3]}"""

data = [("akash", 10), ("gaurav", 12), ("anand", 14),
        ("suraj", 20), ("akhil", 25), ("ashish", 30)]

result = {}
for key, value in data:
    result[key] = [value]
print(result)

#-------------------------------------------------------------

"""14. Write a Python function that takes a list and returns a new list with unique elements of the first list.
	Exercise 1:
	Input:
	[1,2,3,3,3,3,4,5]
	Output:
	[1, 2, 3, 4, 5]"""

def unique_list(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result

lst = [1, 2, 3, 3, 3, 3, 4, 5]
print(unique_list(lst))

#-------------------------------------------------------------------------------

"""
15.  Write a Python program to print the even numbers from a given list.
		Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
		Expected Result : [2, 4, 6, 8]"""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for num in lst:
    if num % 2 == 0:
        result.append(num)
print(result)

#---------------------------------------------------------------------------------

"""16. Write a Python function to check whether a number is perfect or not.¶
	A Perfect number is a number that is half the sum of all of its positive divisors (including itself).
	Example :
	The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6.
	Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6.
	The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128."""


#-----------------------------------------------------------------------------------

"""
17. Write a Python function to concatenate any no of dictionaries to create a new one.
	Sample Dictionary :
	dic1={1:10, 2:20}
	dic2={3:30, 4:40}
	dic3={5:50,6:60}
	Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""

def merge_dicts(*dicts):
    result = {}
    for d in dicts:
        result.update(d)
    return result

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

print(merge_dicts(dic1, dic2, dic3))

#-----------------------------------------------------------------------------------

"""18. Write a python function that receives a list of integers and prints out a histogram of bin size 10

	Input:
	[13,42,15,37,22,39,41,50]
	Output:
	{11-20:2,21-30:1,31-40:2,41-50:3}"""