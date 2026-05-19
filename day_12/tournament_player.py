# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
all_three_match = match1 & match2 & match3
# 2. Find players who participated in exactly two matches
two_match = ((match1 & match2) | (match2 & match3) | (match3 & match1)) - all_three_match
# 3. Find players who participated in only one match
one_match = (match1 - match2 - match3) | (match2 - match3 - match1) | (match3 - match2 - match1)
# 4. Count total unique players
total_players = match1 | match2 | match3
total = len(total_players)
# 5. Find players in Match 1 only
match1_player = match1 - match2 - match3
# Print results in the specified format
print(f"Players in all matches: {sorted(list(all_three_match))}")
print(f"Players in exactly two matches: {sorted(list(two_match))}")
print(f"Players in only one match: {sorted(list(one_match))}")
print(f"Total unique players: {total}")
print(f"Players in Match 1 only: {sorted(list(match1_player))}")








