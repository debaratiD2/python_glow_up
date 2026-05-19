cubes = [x**3 for x in range(1, 6)]
print(cubes)
# Output: [1, 8, 27, 64, 125]

#creating a list of strings from characters ✅✅
chars = [char for char in 'hello']
print(chars)

#list of even numbers
numbers = [number for number in range(2, 11, 2)]
print(numbers)

#Convert all items in a list to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = [fruits.upper() for fruits in fruits]
print(uppercase_fruits)

#Create a function named get_word_lengths that takes a list of words as an argument and returns a list of the lengths of each word using a list comprehension

def get_word_lengths(words):
    word_len = [len(word) for word in words]
    return word_len  

input_words = ['hello', 'world', 'python']
lengths = get_word_lengths(input_words)
print(lengths)


#Create a function named filter_and_square that takes a list of numbers numbers as an argument. The function should use a list comprehension to create a new list that includes the squares of only the positive numbers from the original list. The function should return the new list
def filter_and_square(numbers):
    # Write code here
    filterd_list = [n**2 for n in numbers if n > 0]
    return filterd_list

input_numbers = [-2, -1, 0, 1, 2]
result = filter_and_square(input_numbers)
print(result)