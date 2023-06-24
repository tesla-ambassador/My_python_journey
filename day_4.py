rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user_input = int(input('What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors\n'))
symbols_array = [rock, paper, scissors]

if user_input < 0 or user_input > 2:
  print('Invalid input')
else:
  print(symbols_array[user_input])
  computer_input = random.randint(0, 2)
  print(f'Computer chose:\n{symbols_array[computer_input]}')
  if computer_input == 0 and user_input == 2:
    print('You lose')
  elif computer_input == 1 and user_input == 2:
    print('You win')
  elif computer_input == 2 and user_input == 0:
    print('You lose')
  elif user_input == 0 and computer_input == 2:
    print('You win')
  elif user_input == 1 and computer_input == 2:
    print('You lose')
  elif user_input == 1 and computer_input == 0:
    print('You win')
  elif computer_input == 1 and user_input == 0:
    print('You lose')
  else:
    print("It's a tie")