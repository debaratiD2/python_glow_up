def create_student_dict(name, age, major):
    # Write code here
    dictionary = {
        "name": name,
        "age": age,
        "major": major
    }
    return dictionary

call1 = create_student_dict("Alice", 20, "Computer Science")
print(call1)

def get_capital(country_capitals, country_name):
    # Write code here
    result = country_capitals[country_name]
    return result

call2 = get_capital({"USA": "Washington, D.C.", "France": "Paris", "Japan": "Tokyo"}, "France")
print(call2)

recipe_book = {
    "Pancakes": ["flour", "milk", "eggs", "sugar"],
    "Salad": ["lettuce", "tomato", "cucumber", "olive oil"]
}
print(recipe_book['Pancakes'])
recipe_book["Smoothie"] = ["banana", "milk", "honey"]
recipe_book["Smoothie"].append("blueberries")
print(recipe_book)