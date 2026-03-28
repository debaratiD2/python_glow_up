'''A nested dictionary is a dictionary within a dictionary, allows you to organize complex data structures, making it easier to work with related information.
Helpful when you need group related info together.'''

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"}
}


print(students["Alice"]["age"])  

# Adding a new key-value pair to a nested dictionary
students["Alice"]["major"] = "Math"
print(students["Alice"])  # Output: {'age': 20, 'grade': 'A', 'major': 'Math'}

# in keyword -->simple ways to check for the presence of keys in a dictionary

my_dict = {'name': 'Alice', 'age': 30}

if 'name' in my_dict:
    print("Name exists in the dictionary.")

if 'city' in my_dict.keys():
    print("City exists in the dictionary.")
else:
    print("City does not exist in the dictionary.")
