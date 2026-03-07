# popular form of loops in python that allows to iterate over the fulfillment of a certain condition.

# example - 01
# Print the first number that is smaller than 3.5 after repeatedly dividing a float input by 2.

num_1 = float(input())
while num_1 >= 3.5:
    num_1 /= 2
if(num_1 < 3.5):
        print(num_1)
