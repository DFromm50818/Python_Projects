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

print("Welcome to Rock, Paper and Scissors.")

choices_str = [rock, paper, scissors]
choices_int = [0, 1, 2]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.choice(choices_int)

if (player_choice >= 3) or (player_choice < 0):
  print("You typed a invalid number, Computer wins!")
  
else:  
  print("\nPlayer\n" + choices_str[player_choice])
  print("Computer\n" + choices_str[computer_choice]) 

  if (player_choice == 0) and (computer_choice == 2):
    print("Player wins!")
    
  elif (player_choice == 1) and (computer_choice == 0):
    print("Player wins!")
  
  elif (player_choice == 2) and (computer_choice == 1):
    print("Player wins!")
  
  elif player_choice == computer_choice:
    print("Draw!")
  
  else:
    print("Computer wins!")