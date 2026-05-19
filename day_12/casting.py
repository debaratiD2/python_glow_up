'''
convert a list to a set using the set()
Casting to a set transforms the list into a set, which contains only unique elements
'''
def remove_duplicates(numbers):
    # Write code here
    
    new_list = list(set(numbers))
    
    return new_list

# Example usage
my_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(my_list)
print(result)  # Output: [{1, 2, 3, 4,