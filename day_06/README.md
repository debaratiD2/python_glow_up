
# String and his pattern 🙄

Imagine I’m looking for the word **'aba'** in a long string of letters. I take a magnifying glass that is exactly three letters wide. I start at the very beginning, look through the glass, and ask: 'Does this match?' Then, I slide the glass over by **just one letter** and ask again. Every time I see a match, I write down the position where my glass started.

So I just started solving this by:
1. **The Pre-Check** : Check if the pattern is empty or longer than the text. 
                                 If it is, stop and return **False/Zero/Empty** immediately.
2. The Setup: Create an empty list to store the indices where match is found.
                         `positions = []`
3. Sliding Rule: Start at the beginning of the text and move according to the pattern[one character at a time]
                 `for i in range(len(text) - len(pattern)+1):`
                 `**positions = []**`
3. Sliding Rule: Start at the beginning of the text and move according to the pattern[one character at a time]
                 `**for i in range(len(text) - len(pattern)+1):**`

4. Comparison: At every single character, look at the slice of text inside the pattern. 
                           If it matches the pattern exactly, add that starting position to the list.
                 **`if text[i:i+len(pattern)] == pattern`
                   `positions.append(i)`**
5. Conclusion: Check the final list: if it’s not empty, set the result to **True**, 
                                                   count how many items are in the list, 
                                                   return everything as a tuple.

```
found = len(positions) > 0
count = len(positions)
return(found, count, positions)
```

| Concept | Explanation | Example | Formula |
| ----- | ----- | ----- | ----- |
| **What if we run text\[i:range(len(text))+1\]?** | this would simply cause an **index out of range** error when checking near the end, because the slice **text\[i:i+len(pattern)\]** would extend beyond the string. | text \= "hello" (len=5),  pattern \= "ll" (len=2) **If i \= 4, slice would be text\[4:6\] → index 6 doesn't exist.** | You need to ensure the **last starting position** leaves enough characters for the full pattern. |
| Why exactly **(len(text) \- len(pattern)+1 ??** | The last index where you can start and still have **len(pattern)** characters left is **len(text) \- len(pattern)**. | For "hello" and **"ll":** last start \= 5 \- 2 \= **3** Starting at 3 → slice **text\[3:5\]** \= **"lo"** (safe). | last\_start \= len(text) \- len(pattern) num\_starts \= len(text) \- len(pattern) \+ 1 |
| **The loop range** | To iterate over all valid starts, use  **range(len(text) \- len(pattern) \+ 1\)** | **range(5 \- 2 \+ 1\) \= range(4)** → yields 0,1,2,3. | **range(len(text) \- len(pattern) \+ 1\)** |
| **Slicing to compare** | At each start index i, take the substring from i to i+len(pattern) and compare with the pattern. | i=0 → text\[0:2\] \= "he" ≠ "ll"i=2 → text\[2:4\] \= "ll"  | **text\[i : i \+ len(pattern)\] \== pattern** |
| **Finding overlapping matches** | By moving the start index by **only 1** each time, you can detect overlapping patterns ("aaa" with pattern "aa" gives positions 0 and 1). | text \= "aaaa", pattern \= "aa" i=0 → slice "aa"  i=1 → slice "aa"  i=2 → slice "aa"→ positions \[0,1,2\]. | Overlaps are included because we don't skip ahead. |
| **Edge case: pattern longer than text** | If len(pattern) \> len(text), no starting position works. | text \= "hi", pattern \= "hello" → loop would be range(2-5+1) \= range(-2) → empty, so the positions list stays empty. | Always handle this case first:  **if len(pattern) \> len(text): return (False, 0, \[\])** |
| **Empty pattern** | If a pattern is empty, some definitions might say it matches everywhere, but usually we treat it as not found. | pattern \= "" → we return (False, 0, \[\]) to avoid confusion. | Check **if not pattern: return (False, 0, \[\])** |

