def merge(lst1, lst2):
    combined = lst1 + lst2
    return sorted(combined)  #combined.sort()

lst1 = [1, 2, 3]
lst2 = []
result = merge(lst1, lst2)
print(result)

def prod(lst):
    # Write code here
    prod = 1
    for i in range(len(lst)):
        prod *= lst[i]
    return prod

lst = [12, 23, 56, 2, -18, 98]

result = prod(lst)
print(result)

def reverse(lst):
    rev_list = []
    for i in range(len(lst)-1,-1,-1):
        rev_list.append(lst[i])
    return rev_list
lst = [1, 2, 3, 4, 5]
result = reverse(lst)
print(result)

def reverse(numbers):
    # Return the reversed list
    return numbers[::-1]

def reverse(numbers):
    # Convert the reversed iterator to a list and return it
    return list(reversed(numbers))

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    if len(fruit) > 5:
        print(fruit)

lst = input().split(",")
# Write your code below
new_list = []
for words in lst:
    if len(words) > 5:
        new_list.append(words)
print(new_list)