# 4. Running Sum on list Write a program to print a list after performing running sum on it.

# 	i.e:

# 	Input:

# 	list1 = [1,2,3,4,5,6]
# 	Output:

# 	[1,3,6,10,15,21]

list1 = [1, 2, 3, 4, 5, 6]

running_sum = []
total = 0

for num in list1:
    total += num
    running_sum.append(total)

print(running_sum)
