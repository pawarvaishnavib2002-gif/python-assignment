# 7. Sort a list of alphanumeric strings based on product value of numeric character in it. If in any string there is no numeric character take it's product value as 1.

# 	Input:

# 	['1ac21', '23fg', '456', '098d','1','kls']
# 	Output:

# 	['456', '23fg', '1ac21', '1', 'kls', '098d']
def product_value(s):
    prod = 1
    has_digit = False
    
    for ch in s:
        if ch.isdigit():
            prod *= int(ch)
            has_digit = True
    
    return prod if has_digit else 1


data = ['1ac21', '23fg', '456', '098d','1','kls']

result = sorted(data, key=product_value, reverse=True)

print(result)