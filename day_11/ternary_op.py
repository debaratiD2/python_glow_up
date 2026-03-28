'''
syntax: value_if_true if condition else value_if_false
If the condition is true, the expression evaluates to value_if_true.
If the condition is false, the expression evaluates to value_if_false.

'''
#example 1
age = 20
status = "Eligible" if age >= 18 else "Not Eligible"
print(status)

#example 2
score = int(input())
print("Pass" if score >= 50 else "Fail")



