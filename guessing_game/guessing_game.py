# Guessing game algorithm
# 1. Ask user to choose difficulty.
# 2. if it's easy, then attempts == 5
# 3. else attempts == 5
# 4. Generate a random number
# 5. Ask the user to guess the number between 1 and 100
# 6. If I am close to the answer but less than it, I shall print too low
# 7. If I am close to the answer but more than it, I shall print too high.
# 8. Repeat 5-7 while reducing the number of lives at each loop cycle when I don't arrive at the answer.
# 9. If I arrive at the answer before I run out of lives then I have won
# 10. Else I have lost.

import random
import os
# Function to clear the console.
clear = lambda: os.system('clear')
print('Welcome to the guess_the_number game!')
difficulty_level = input('Please choose your preffered difficulty level (Hard) or (Easy): ').lower()

guess = random.randint(1, 100)

def guess_the_number():
    if difficulty_level == 'hard':
        lives = 5
    else:
        lives = 10
    while lives != 0:
        user_guess = int(input('Please guess a number between 1 and 100: '))
        if user_guess == guess:
            clear()
            print(f'You guessed {user_guess} and the answer was {guess}\nCongratulations, you have won!')
            return
        elif user_guess < guess:
            clear()
            lives -= 1
            print(f"That's too low\nYou are left with {lives} lives")
        else:
            clear()
            lives -= 1
            print(f"That's too high\nYou are left with {lives} lives")
    if lives == 0:
        clear()
        print("You are out of lives, sorry you've lost!")
        
guess_the_number()
    
