# Algorithm
# 1. Import relevant data and libraries.
# 2. Create a variable to store user input
# 3. Create a variable to store the final score
# 4. Loop through the data.
# 5. Create an array to compare the two varables.
# 6. If a user wins, pop off the last element and add another random element
# 7. else if he fails, end the loop and print user's final score.

import random
from game_data import data
from art import logo, vs
import os
clear = lambda: os.system('clear')

final_score = 0
still_playing = True
comparisons = [data[random.randint(0, 49)]]
while still_playing:
    person_2 = data[random.randint(0, 49)]
    if comparisons[0] == person_2:
        person_2 == data[random.randint(0, 49) + 1]
    comparisons.append(person_2)
    print(logo)
    print(f"Compare A: {comparisons[0]['name']}, a {comparisons[0]['description']} from {comparisons[0]['country']}")
    print(vs)
    print(f"Compare B: {comparisons[1]['name']}, a {comparisons[1]['description']} from {comparisons[1]['country']}")
    user_input = input("Who has more followers 'A' or 'B': ").lower()
    if user_input == 'a':
        if comparisons[0]['follower_count'] > comparisons[1]['follower_count']:
            final_score += 1
            comparisons.pop(0)
            clear()
        else:
            still_playing = False
            clear()
            print(logo)
            print(f'Sorry you lost with a final score of: {final_score}')
    else:
        if comparisons[1]['follower_count'] > comparisons[0]['follower_count']:
            final_score += 1
            comparisons.pop(0)
            clear()
        else:
            still_playing = False
            clear()
            print(logo)
            print(f'Sorry you lost with a final score of {final_score}')
                     