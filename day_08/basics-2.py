#placeholder
for _ in range(5):
    print(_)

#round(number, ndigits)
print(round(3.14159))
print(round(3.14159, 3))
print(round(3.14159, -1))
'''Python rounds halfway cases to the nearest even number'''
print(round(2.5))
print(round(3.5))

#list() --> converts an iterable to a list
print(list('hello'))
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3]

my_range = range(5)
my_list = list(my_range)
print(my_list)  # [0, 1, 2, 3, 4]