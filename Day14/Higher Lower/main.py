import random
import art
from game_data import data

def cards():
    #randomnr = random.randint(0, 49)
    #cards = data[randomnr]
    cards = random.choice(data)
    return cards

while True:
    print(art.logo)
    player_score = 0
    game_status = input("Do you want to play Higher and Lower? For yes 'y' and for no 'n': ")
    first_card = cards()
    if game_status == "n":
        print("Have a nice day!")
        break

    while game_status == "y":

        second_card = cards()

        if first_card == second_card:
            second_card = cards()

        if game_status == "n":
            print("Have a nice day!")
            break

        print(f"\nPlayer Score: {player_score}\n")

        print("Name: ",first_card['name'],"\nFollower Count: ",first_card['follower_count'],"\nDescritpion: ",first_card['description'],"\nCountry: ",first_card['country'])
        print(art.vs)
        print("Name: ",second_card['name'],"\nFollower Count: ?","\nDescritpion: ",second_card['description'],"\nCountry: ",second_card['country'])

        print("\nHas",second_card['name'], "higher or lower follower count? \n'h' for higher or 'l' for lower: ")
        player_choice = input("")

        if player_choice == "h" and first_card['follower_count'] < second_card['follower_count']:
           player_score += 1
           print("Higher was right. Congratulations for your Point! Follower Count was: " ,second_card['follower_count'])
           first_card = second_card

        elif player_choice == "l" and first_card['follower_count'] > second_card['follower_count']:
             player_score += 1
             print("Lower was right. Congratulations for your Point! Follower Count was: " ,second_card['follower_count'])
             first_card = second_card

        else:
            print(f"Player Score: ", player_score)
            print("That was wrong. You Lose!")
            break




