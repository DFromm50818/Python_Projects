#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
import art

#Generates a random number
def random_number():  
  return int(random.random()*99)

#Function for difficulty
def difficult(decision):
  if decision == "easy":
    return 10
  elif decision == "hard":
    return 5

# Check winning condition
def number_check(number):
  if number == guess_number:
    print("That is the right number. You win.")
    return 1
  elif number < guess_number:
    print("Number is too low.")
  elif number > guess_number:
    print("Number is too high.")


game = True

#Main program reapetable
while(game):
  print(art.logo)
  print("Welcome to Guess my number Game.")
  print("Find the number between 0 and 100.")
  guess_number = random_number()
  user_difficult = difficult((input("Type 'easy' for 10 attempts or 'hard' for 5 attempts. ")))
  user_attempts = user_difficult
  #print(f"The Number: {guess_number}")
  lose_condition = 0
  
  for counter in range(user_difficult):
    print(f"You habe {user_attempts} attempts remaining to guess the number.")
    user_input = int(input("Make a guess: "))
    if number_check(user_input) == 1:
      lose_condition += 1
      break
    user_attempts -= 1
    
  if lose_condition == 0:
      print("You lose.") 
    
  if input("You want to play a new round? Type 'yes' or 'no'. ") == "no":
    print("Have a nice day.")
    game = False

    
    
    