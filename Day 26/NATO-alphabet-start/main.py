# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
print(data)
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

for (index, row)in data.iterrows():
    print(f"row.letter: {row.letter}, row.code: {row.code}")
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
for letter_1 in word:
    print(phonetic_dict[letter_1])
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
