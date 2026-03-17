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

