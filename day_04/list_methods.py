'''
append(element) - adds a single element to the end of the list
clear() - removes all elements from the list
pop(index) - removes an element at the specified index
reverse() - reverses the order of the list
sort() - sorts the list in ascending order
'''
lst1 = [1, 2]
lst2 = [3, 4]
lst1.append(lst2)  # Wrong approach for merging
print(lst1)  # Output: [1, 2, [3, 4]] - lst2 is nested inside!
my_list = ["orange", "banana", "apple"]
my_list.append("strawberry")
print(my_list)

#clear() method removes all the elements from the list, leaving it empty
my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)

# pop() method removes an element at the specified index and returns it.
# If no index is specified, it removes and returns the last element.
my_list = [1, 2, 3, 4, 5]
removed_element = my_list.pop(2)  # Removes the element at index 2 (which is 3)
print(removed_element)  # Output: 3
print(my_list)  # Output: [1, 2, 4, 5

#sort() method sorts the list in ascending order
my_list = [1, 9, 2, 3]
my_list.sort()
print(my_list)

'''enumerate() is a more elegant way to get both index and value:kinnda like map(index, value) but for lists'''
fruits = ["apple", "banana", "orange"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

lst = list(map(int, input().split(",")))
# Write your code below
new_lst = []
for index, value in enumerate(lst):
    if(value % 5 == 0) or (value < 50):
        new_lst.append(index)
print(new_lst)

'''The split() method divides a string into a list of substrings based on a delimiter.
'''
text = "apple banana cherry"
fruits = text.split()
print(fruits)
# ['apple', 'banana', 'cherry']
'''The join() method is used to concatenate a list of strings into a single string, with a specified separator between each element.'''
words = ['Hello', 'World', 'Python']
text = ' '.join(words)
print(text)
# "Hello World Python"
