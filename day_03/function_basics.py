def print_large_number():
    print("50005000")

n = int(input())
for i in range(n):
    # Call the function here
    print_large_number()

def multiply(a,b):
    return a*b
a = int(input())
b = int(input())
result = multiply(a,b)
print(result)

def square_number(n):
    return n*n
input_num = int(input())
result = square_number(input_num)
print(result) 