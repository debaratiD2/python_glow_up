def find_occurrences(text, pattern):
    # Write your code here
    if not pattern or len(pattern) > len(text):
        return(False, 0, [])
    positions = []
    for i in range(len(text) - len(pattern)+1):
        if text[i:i+len(pattern)] == pattern:
            positions.append(i)
    found = len(positions) > 0
    count = len(positions)
    return(found, count, positions)
    pass

# Read input
text = input()
pattern = input()

# Call your function and print the result
result = find_occurrences(text, pattern)
print(result)