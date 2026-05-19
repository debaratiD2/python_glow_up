def manage_set(set1, element_to_add, element_to_remove):
    # Write code here
    set1.add(element_to_add)
    if element_to_remove in set1:
        set1.remove(element_to_remove)
    if 5 in set1:
        print("5 is in the set")
    else:
        print("5 is not in the set")

# Example usage
#my_set = {5, 6, 7}
#manage_set(my_set, 8, 5)  
#print(my_set)  

'''remove the element that are greater than 10 from the set'''

def iterate_and_filter_set(input_set):
    # Write code here
    new_set = set()
    for element in input_set:
        if element <= 10:
            new_set.add(element)
    return new_set
# Example usage
my_set = {5, 12, 7, 15, 3, 10}
result = iterate_and_filter_set(my_set)
print(result)  # Output: {3, 5, 8}