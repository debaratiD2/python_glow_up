'''sorted() function--> takes an iterable (e.g., a list, tuple, or set) as its argument and returns a new list containing the sorted elements. 
By default, it sorts in ascending order.'''
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(sorted_numbers)

#for descending order: sorted(numbers, reverse = True)
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers_desc = sorted(numbers, reverse=True)
print(sorted_numbers_desc)

#sorted_strings: based on their lexicographical order 
words = ["apple", "banana", "cherry"]
sorted_words = sorted(words)
print(sorted_words)

#custom_sorting with key function: sorted(words, key = len)

words = ["apple", "bananaan", "cherry"]
sorted_words_by_length = sorted(words, key=len)
print(sorted_words_by_length)
# Output: ['apple', 'cherry', 'bananaan']
