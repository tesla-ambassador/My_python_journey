import random
import os
from blackjack_art import logo

clear = lambda: os.system('clear')

def initiate_game():    
    print(logo)
    player_cards = {
        "user": [random.randint(1, 10), random.randint(1, 10)],
        "computer": [random.randint(1, 10), random.randint(1, 10)]
    }
    print(f'Your cards are {player_cards["user"]}')
    print(f"The computer's first card is {player_cards['computer'][0]}")

    lives = 5

    should_continue = True
    while should_continue and lives > 0:
        user_sum = sum(player_cards["user"])
        computer_sum = sum(player_cards['computer'])
        
        user_diff = 21 - user_sum
        computer_diff = 21 - computer_sum
        
        def printCards():
            print(f'Your cards are {player_cards["user"]}')
            print(f"The computer's cards are {player_cards['computer']}")
        
        if user_sum == 21:
            clear()
            printCards()
            print('Congratulations, you win')
            should_continue = False
        elif user_sum > 21:
            clear()
            printCards()
            print('Sorry, you lose.')
            should_continue = False
        elif computer_sum == 21:
            clear()
            printCards()
            print('Sorry, you lose')
            should_continue = False
        elif computer_sum > 21:
            clear()
            printCards()
            print('Congratulation, you win')
            should_continue = False
        else:
            another_one = input('Do you want to draw another card (y) or (n)? ')
            if another_one == 'y':
                player_cards["user"].append(random.randint(1, 10))
                player_cards["computer"].append(random.randint(1, 10))
                print(f'Your cards are {player_cards["user"]}')
                print(f"The computer's first card is {player_cards['computer'][0]}")
                lives -= 1  
            else:
                clear()
                printCards()
                if user_diff > computer_diff:
                    print('Sorry, you lose!')
                    should_continue = False
                elif user_diff < computer_diff:
                    print('Congratulations, you win!')
                    should_continue = False
                else:
                    print('It\'s a draw!')
                    should_continue = False
    play_again = input('Do you want to play again? (y) or (n)\n')
    if play_again == 'y':
        initiate_game()
    else:
        print('Thank you playing')
        return        

play_game = input('Do you want to play blackjack? (y) or (n)\n')
if play_game == 'y':
    initiate_game()