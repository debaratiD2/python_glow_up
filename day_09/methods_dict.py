#keys()--> Returns a view object that displays a list of all the keys in the dictionary
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
keys = my_dict.keys()
print(keys)

#values()--> Returns a view object that displays a list of all the values in the dictionary
values = my_dict.values()
print(values)

#items()--> Returns a view object that displays a list of a dictionary's key-value tuple pairs
items = my_dict.items()
print(items)

#get(key, default): Returns the value for the specified key. If the key is not found, it returns the default value
age = my_dict.get('age')
print(age)     # Output: 30


country = my_dict.get('country', 'USA')
print(country)   # Output: USA

city = my_dict.pop('city')
print(city)    # Output: 'New York'

print(my_dict)     # Output: {'name': 'Alice', 'age': 30}

