#nested - loop
# Get input for rows and columns
rows = int(input())
cols = int(input())

# Write your nested loops here
# Outer loop for rows
# Inner loop for columns
for i in range(rows):
    line = ""
    for j in range(cols):
        line += "*"
    print(line)   
'''a program that gets a dynamic number of input values.

The first input tells you how many numbers will follow. The next inputs are whole numbers that you need to sum.

In the end, print the sum of all the input numbers (not including the first input.'''
test = int(input())
sum = 0
for i in range(test):
    num = int(input())
    sum += num
print(sum)    