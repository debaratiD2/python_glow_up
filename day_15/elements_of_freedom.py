def elements_of_freedom(elements):
    new_elements = []
    # Step 1: Filter elements with length >= 5
    filter_1 = [item for item in elements if len(item) >= 5]
    # Step 2: Convert filtered elements to uppercase
    filter_2 = [item.upper() for item in filter_1]
    # Step 3: Create a list of unique elements
    new_elements = list(dict.fromkeys(filter_2))
    # Step 4: Return the final result
    
    return new_elements
    pass


input_elements = ["repeat", "repeat", "unique", "words", "words", "filter"]


result = elements_of_freedom(input_elements)
print(result)

'''You can maintain order by using dict.fromkeys() directly on the uppercase list instead of using set(). This way, you can create a list of unique elements while preserving the original order of the uppercase elements.'''