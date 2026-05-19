'''Create a function named house_of_lists that takes a list of lists list_of_lists as an argument. Each inner list contains numbers. The function should use list comprehensions to perform the following operations:

1. Filter out inner lists that have a sum greater than 50, keeping only those whose sum is 50 or less.
2. From the remaining inner lists, extract numbers that are less than 5.
3. Combine all extracted numbers into a single list.
4. Return the combined list of numbers.'''



def house_of_lists(list_of_lists):
    filtered_list = [item for inner_list in list_of_lists if sum(inner_list) <= 50 
                     for item in inner_list if item < 5]

    return filtered_list

input_lists = [[5, 5, 5, 5, 5], [1, 1, 1, 1], [2, 2, 2, 2], [50, 1]]
result = house_of_lists(input_lists)
print(result)