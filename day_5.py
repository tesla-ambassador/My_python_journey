#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
password_hard = []
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
    random.shuffle(letters)
    password.append(letters[i].lower())
for i in range(0, nr_symbols):
    random.shuffle(symbols)
    password.append(symbols[i])
for i in range(0, nr_numbers):
    random.shuffle(numbers)
    password.append(numbers[i])
password = ''.join(password)
print(f'This is the easy method of getting the password {password}')
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
for i in range(0, nr_letters):
    random.shuffle(letters)
    password_hard.append(letters[i].lower())
for i in range(0, nr_symbols):
    random.shuffle(symbols)
    password_hard.append(symbols[i])
for i in range(0, nr_numbers):
    random.shuffle(numbers)
    password_hard.append(numbers[i])
password_hard = ''.join(random.sample(password_hard, len(password_hard)))

print(f'We used the hard method to get the password here: {password_hard}')

## we can also use the random.choice method.
# for i in range(0, nr_letters):
#     random.choice