'''print n - pyramid using * where n is an odd number.'''
n = int(input())
rows = (n+1)//2
for i in range(1, rows+1):
    stars = 2 * i - 1
    print("*" * stars)
