'''Create a program that receives a list as input (given) and prints the following sliced list (depends on the list length):

For odd-length lists: take the middle item and one item on each side (3 items total)
For even-length lists: take the two middle items
When dividing numbers:

/ gives you a decimal number (5/2 = 2.5)
// removes the decimal part (5//2 = 2)
For this challenge, use // because list slicing only works with whole numbers.'''
lst = input().split(",")
length = len(lst)
middle_index = length // 2
final_lst = []
if length &1:
    print(lst[middle_index - 1:middle_index+2])
else:
    print(lst[middle_index-1:middle_index+1])