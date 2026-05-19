#sum()
'''The sum() function is a built-in function that allows you to quickly calculate the sum of elements in an iterable, such as a list or a tuple.'''

#example-1
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)
# Output: 15

#example-2
'''You can also provide a second argument to sum(), which serves as the starting value for the sum.'''
numbers = [1, 2, 3, 4, 5]
total = sum(numbers, 10)
print(total)
# Output: 25





#example-3
sales = eval(input())
starting_cash = eval(input())

# Write code here
total = sum(sales, starting_cash)
print(total)