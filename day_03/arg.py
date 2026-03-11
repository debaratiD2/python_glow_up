# function for calculating the sum of the first n natural numbers
def sigma(n):
    result = (n * (n+1)) / 2
    return int(result)

n = int(input())
result = sigma(n)
print(result)


#function to check whether the username and password are valid
def is_valid(username, password):
    # Write code here
    if username == "admin":
        return True
    elif (username == "admin" or username == "user") and (password=="user" or password=="qweasd"):
        return True
    else:
        return False
    
username = input()
password = input()
result = is_valid(username, password)
print(result)

