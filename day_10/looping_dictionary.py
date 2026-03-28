my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(f"{key}: {value}")

'''The first loop iterates over the keys of the dictionary keys()
   The second loop iterates over the values using the values() method
   The third loop uses the items() method to iterate over both keys and values simultaneously'''

def print_employee_details(employee_data):
    
    if employee_data == {}:
        print("No data available")
    else:
        for key, value in employee_data.items():
            print(f"{key}: {value}")

#employee_info = {"name": "Bob", "age": 25, "department": "Engineering"}
employee_data = {}
print_employee_details(employee_data)