#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

user_guess = input("Which letter you choose? ")
lower_user_guess = user_guess.lower()

print (lower_user_guess)
print (chosen_word)

if lower_user_guess in chosen_word:
  print("You are right.")
else:
  print('''
        \o/
        ''')



#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
