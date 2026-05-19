#new_list = [expression for item in iterable]
numbers = [1, 2, 3, 4, 5]
squares = [n * n for n in numbers]
print(squares)


#example-2
def double_numbers(numbers):
    # Write code here
    new_list = [n*2 for n in numbers]
    return new_list

input_numbers = [1, 2, 3, 4, 5]
result = double_numbers(input_numbers)
print(result)