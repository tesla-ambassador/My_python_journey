import pandas as pd

statement = input('Please input a word: ').upper()

df = pd.read_csv('NATO-alphabet-start/nato_phonetic_alphabet.csv')
name_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name_list = [letter for letter in statement]

result = [word for letter in name_list for (key, word) in name_dict.items() if letter == key] 

print(f'result: {result}')
