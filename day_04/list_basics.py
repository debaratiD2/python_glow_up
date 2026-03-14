# collection of different types of items[numbers, strings, and more]
# []--> used to create a list, separated by commas
#each item in the list is called an element
#position of each element is called index, starts from 0
my_list = [1, 2, "three", True]
print(my_list)
length = len(my_list) # len() method is used to find out the length of the list
print(length)
#accessing elements in the list
def values(lst):
    # Write code here
    for i in range(len(lst)):
        print(lst[i])


def change_element(lst, index, new_element):
    # Write code here
    lst[index] = new_element
    return lst
my_list = [1, 2, "three", True]
change_element(my_list, 2, "four")
print(my_list)