#Calculating the Sum of Squares
numbers = [1, 2, 3, 4, 5]
sum_of_squares = sum([n**2 for n in numbers])
print(sum_of_squares)

#Finding the Minimum of Transformed Values
numbers = [-3, -1, 0, 1, 3]
min_absolute = min([abs(n) for n in numbers])
print(min_absolute)

#Finding the Maximum of Filtered Values
numbers = [1, 2, 3, 4, 5, 6]
max_even = max([n for n in numbers if n % 2 == 0])
print(max_even)

#Calculating the sum of Positive Numbers
def sum_positive_evens(numbers):
    filter_positive = sum([n for n in numbers if n > 0 and n % 2 == 0])
    return filter_positive

input_numbers = [-10, -5, 0, 2, 4, 7, 10, 12]
result = sum_positive_evens(input_numbers)
print(result)