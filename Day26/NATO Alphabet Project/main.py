import pandas

df_nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
dict_nato_alphabet = dict(df_nato_alphabet.values)

user_word = input("Enter a Word: ")

print([dict_nato_alphabet[letter] for letter in user_word.upper()])
