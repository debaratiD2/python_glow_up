text = "Hey"
for char in text:
    print(char)

for i in range(len(text)):
    print(f"position {i}: {text[i]}")


text = input()

count = 0
for char in text:
    if char.lower() == "p":
        count += 1

print(count)

text = input()
delimiter = input()
words = text.split()
new_string = delimiter.join(words)
print(new_string)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:6])
print(numbers[:5])
print(numbers[5:])
print(numbers[::2]) # every second element
print(numbers[::-1]) # Reverses the list. The slice [::-1] creates a new list that starts from the end and goes  #to the beginning, effectively reversing the order of the elements.