# 8. Write a program that can find the max number of each row of a matrix
# 	Example:

# 	Input:

# 	[[1,2,3],[4,5,6],[7,8,9]]
# 	Output

matrix = [[1,2,3],[4,5,6],[7,8,9]]

result = []

for row in matrix:
    result.append(max(row))

print(result)