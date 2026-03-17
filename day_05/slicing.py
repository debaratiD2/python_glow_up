numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2]) # every second element
print(numbers[::-1]) # Reverses the list. The slice [::-1] creates a new list that starts from the end and goes  #to the beginning, effectively reversing the order of the elements.

##lst[start:stop:step]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[1:8:2])
# Output: [1, 3, 5, 7]
print(numbers[2::3])
# Output: [2, 5, 8]
print(numbers[-3:]) #counting from end; -3 means "start 3 positions from the end"
# Output: [7, 8, 9]
print(numbers[:-4]) #counting from end; -4 means "stop 4 positions from the end"
# Output: [0, 1, 2, 3, 4, 5, 6]
print(numbers[::3]) #every third element
# Output: [0, 3, 6, 9]
print(numbers[1::4]) #every fourth element starting from index 1
# Output: [1, 5, 9]

'''Create a program that receives a list as input (given) and prints three new lists based on the following slicing operations:
A list containing every third element, starting from index 1 (the second element)
A list containing all the elements from the 6th element to the 1st in reverse order
A list containing every second element starting from the middle of the list to the end'''
'''lst = input().split(",")
print(lst[1::3])
print(lst[5::-1])
middle_index = len(lst) // 2
print(lst[middle_index::2])'''

"Concatenation operator +"
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)
"Repetition operator *"
repeated_list = list1 * 3
print(repeated_list)

# String concatenation
greeting = "Hello" + " " + "World"  # "Hello World"

# String repetition
stars = "*" * 5  # "*****"

def create_pattern(numbers, repeats):
    # Write your code here
    return (numbers + numbers) *repeats
numbers = [1, 2, 3]
repeats = 2
result = create_pattern(numbers, repeats)

lst1 = input().split(",")
lst2 = input().split(",")
# Write your code below
result = [item for item in lst1 if item not in lst2]
#result = lst1.difference(lst2)
print(result)