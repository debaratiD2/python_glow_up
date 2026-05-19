'''Create a function named dictionary_sorter that takes a dictionary data_dict as an argument. The function should sort the dictionary by its values in ascending order and return a new dictionary containing the sorted key-value pairs.'''
def dictionary_sorter(data_dict):


    sorted_dict = sorted(data_dict.items(), key = lambda item:item[1])
   
    return dict(sorted_dict)

example_dict = {'a': 3, 'b': 1, 'c': 2}
result = dictionary_sorter(example_dict)

print(result)