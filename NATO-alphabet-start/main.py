import pandas as pd

is_invalid = True
while is_invalid:
    try:
        statement = input('Please input a word: ').upper()
        if statement.isalpha() == False:
            raise KeyError
    except KeyError:
        print('Please enter alphabetical letters only')
    else:
        is_invalid = False

df = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')
name_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name_list = [letter for letter in statement]

result = [word for letter in name_list for (key, word) in name_dict.items() if letter == key] 

print(f'result: {result}')
