#break
'''You are given a code that prints the numbers from 1 to 10 (including).
Your task is to add if and break statements so that only the numbers from 1 to 5 will be printed, the loop will exit before printing the numbers from 6 to 10.'''
for i in range(1, 11):
    print(i)
    if i == 5:
        break



#continue
'''You are given a code which prints the numbers from 1 to 20 (including).
Your task is to add if and continue statements so that only the even numbers will be printed (2, 4, 6, ...).'''
for i in range(1, 21):
    if i & 1:
        continue
    print(i)

num = int(input())
fact = 1
for i in range(1, num+1):
    if i == 0 or i == 1:
        fact = 1
    else:
        fact *= i
print(fact)