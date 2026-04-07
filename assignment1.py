# 1. Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# 	Given List:

# 	list1 = ["M", "na", "i", "Ra"]
# 	list2 = ["y", "me", "s", "hul"]
	
# 	Output:

# 	[['M','y'], ['na', me'], ['i', 's'], ['Ra', 'hul']]

list1 = ["M", "na", "i", "Ra"]
list2 = ["y", "me", "s", "hul"]

result = []

for i in range(len(list1)):
    result.append([list1[i], list2[i]])

print(result)