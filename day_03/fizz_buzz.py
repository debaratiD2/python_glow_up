print("Welcome to FizzBuzz!")
def fizzbuzz(n):
    if (n % 3 == 0 and n % 7 ==0):
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n%7 == 0:
        return "Buzz"
    elif "3" in str(n):
        return "Almost Fizz"
    else:
        return str(n)

n = int(input())
for i in range(1, n+1):
    result = fizzbuzz(i)
    print(result)