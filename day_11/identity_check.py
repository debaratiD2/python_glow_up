'''
In Python, the is and is not operators are used to check the identity of objects. Unlike the == operator, which checks if two variables have the same value, the is operator checks if two variables refer to the exact same object in memory.
'''

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # Output: True
print(a is c)  # Output: False. a and c are different list objects with the same values

x = 5
y = 5
z = 10

print(x is not y)  # Output: False
print(x is not z)  # Output: True

'''
Identity checks are particularly useful when you want to determine if two variables are pointing to the same object in memory, rather than just having the same value.
In the example above, a and b refer to the same list object, so a is b returns True. However, c is a different list object with the same values, so a is c returns False. Similarly, x and y are small integers that are often cached by Python, so they may refer to the same object, while z is a different integer.
'''