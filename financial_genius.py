import random

"""
This script emulates a creation of a financil genius. 
Run until you find one (usually 1-3 runs is enough to discover your genius).
"""

def is_winner():
    return random.random() < 0.5

num_players = 1024
num_rounds = 10 # log2(1024)

winnings = [0] * num_players

# Simulate the game for num_rounds rounds
for round in range(num_rounds):
    # Simulate each player's turn
    for player in range(num_players):
        if is_winner():
            winnings[player] += 1

highest_winners = sorted(range(num_players), key=lambda i: winnings[i], reverse=True)[:10]

# Print the list of highest winners in descending order
print("The 10 highest winners are:")
for i, player in enumerate(highest_winners):
    print(f"{i+1}. Player {player+1} with {winnings[player]} winnings")
    if winnings[player]==num_rounds:
        print('  ^^^ found Warren Buffet')
