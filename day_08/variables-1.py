#assigning multiple variables in one line
a, b, c = 1, 2, 3
print(a)  
print(b)  
print(c)  

#assigning the same value to multiple variables
x = y = z = 10
print(x)
print(y)
print(z)

#assigning values from a list to variables 
numbers = [4, 5, 6]
a, b, c = numbers
print(a)  # Output: 4
print(b)  # Output: 5
print(c)  # Output: 6

data = [1, 2, 3]
x, y = data
print(x)  
print(y)  # error: too many values to unpack (expected 2)