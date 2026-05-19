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

'''
Adding an element'''
numbers.add(6)
fruits.add("orange")
print(numbers)
print(fruits)

#removing an element
numbers.remove(3)
fruits.remove("banana")
print(numbers)
print(fruits)

#remove() --> raises an error if it does not exist


#checking if an element is present in the set

print(4 in numbers)
print("banana" in fruits)

#discard() -->Does not raise an error if the element is not found
numbers.discard(10)  # No error, even though 10 is not in the set
print(numbers)

#pop()--> Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

my_set = {1, 2, 3}
element = my_set.pop()  
print(element)
print(my_set)

#clear() --> Removes all elements from the set, leaving it empty.
my_set = {1, 2, 3}
my_set.clear()       
print(my_set)

#iterating over a set
my_set = {1, 2, 3, 4, 5}

for element in my_set:
    print(element)

my_set = {5, 2, 8, 1, 3}
sorted_list = sorted(list(my_set))
for element in sorted_list:
    print(element)