# What’s wrong?

Imagine I’m looking for the word **'aba'** in a long string of letters. I take a magnifying glass that is exactly three letters wide. I start at the very beginning, look through the glass, and ask: 'Does this match?' Then, I slide the glass over by **just one letter** and ask again. Every time I see a match, I write down the position where my glass started.

So I just started solving this by:
1. **The Pre-Check** : Check if the pattern is empty or longer than the text. 
                                 If it is, stop and return **False/Zero/Empty** immediately.
2. The Setup: Create an empty list to store the indices where match is found.
                                               `**positions = []**`
3. Sliding Rule: Start at the beginning of the text and move according to the pattern[one 
                           character at a time]
                                               `**for i in range(len(text) - len(pattern)+1):**`
4. Comparison: At every single character, look at the slice of text inside the pattern. 
                           If it matches the pattern exactly, add that starting position to the list.
                                               **`if text[i:i+len(pattern)] == pattern`
                                                  `positions.append(i)`**
5. Conclusion: Check the final list: if it’s not empty, set the result to **True**, 
                                                           count how many items are in the list, 
                                                           return everything as a tuple.


https://www.notion.so/What-s-wrong-326ac1c14084807aa560df22e01efcbd?source=copy_link#32bac1c14084809bb418f06accbdbc6d
