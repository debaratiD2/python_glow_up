def update_employee_info(employee_dict, key, value):
    # Write code here
    employee_dict[key] = value
    return employee_dict

employee_info = {"name": "Bob", "age": 25, "department": "Engineering"}
updated_info = update_employee_info(employee_info, "position", "Senior Engineer")
print(updated_info)

