'''
A set is a collection of unique elements
cannot contain duplicate values
useful when you need to store a collection of items and ensure that each item appears only once
unordered

if you have a basket of fruits and you want to make sure you only have one of each type, you would use a set
'''
# Creating a set of numbers
numbers = {1, 2, 3, 4, 5}

# Creating a set of strings
fruits = {"apple", "banana", "cherry"}

# Creating an empty set
empty_set = set()

'''
Python handles duplicates automatically. For example, {1, 2, 2, 3} will simply become {1, 2, 3} — the duplicate 2 is silently discarded
'''


# Printing the sets - DONT MODIFY
print(sorted(numbers))
print(sorted(fruits))