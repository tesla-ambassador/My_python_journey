from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# User inputs
print(logo)

# ceasor Function (What the tutor did mixed with what I did on further steps)
def ceasor(start_text, shift_amount, cipher_direction):
    end_text = ""
    if shift_amount > 26:
        shift_amount = shift_amount % 26
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += letter
    print(f'Here is the {direction}d result: {end_text}')
 
should_continue = True   
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceasor(start_text=text, shift_amount=shift, cipher_direction=direction)
    
    restart_prompt = input("Do you want to restart (yes) or (no)?\n").lower()
    if restart_prompt == 'no':
        should_continue = False
        print("Sayōnara 👋")
    

# Ceasor Function (What I did on step 3)
# def ceasor(plain_text, shift_amount, cryptography):
#     cipher_text = ""
#     for i in plain_text:
#         if cryptography == 'encode':
#             new_position = alphabet.index(i) + shift_amount
#             cipher_text += alphabet[new_position]
#         elif cryptography == 'decode':
#             new_position = alphabet.index(i) - shift_amount
#             cipher_text += alphabet[new_position]
#     if cryptography == 'encode':
#         print(f'The encoded message is {cipher_text}')
#     elif cryptography == 'decode':
#         print(f'The decoded text is {cipher_text}')
#     else:
#         print(f'{cryptography} was an invalid input choice\nChoose between encode or decode')

## 1. Look at the text and match each letter of the text that corresponds to the alphabet.
## 2. Shift them by the shift amount
## new_position = alphabet.index(i, 26) - shift_amount - That was how I got my new position for decryption.