import random
import hangman_art
import hangman_words
# Angela Yu's version not entirely though.
chosen_word = random.choice(hangman_words.word_list)
display = ['_']*len(chosen_word)
display_joined = ''.join(display)
print(hangman_art.logo)
print(f"The word to guess is: {display_joined}")
typed_words = []
lives = 6

while '_' in display:
    guess = input("Guess a letter: ").lower()
    counter = 0
    if guess in typed_words:
        print('You already guessed this letter!')
    for i in chosen_word:
        if i == guess:
            display[counter] = i
            typed_words.append(i)
        counter += 1
    if guess not in chosen_word:
        print(hangman_art.stages[lives])
        lives -= 1
    if lives < 0:
        print('You have lost the game')
        print(f'The word was ${chosen_word}')
        break
    message = ''.join(display)
    if message == chosen_word:
        print(f'The word is ${message}')
        print('Kudos, you have won the game!')
        break
    print(f'This is the word so far ${message}')  