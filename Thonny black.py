import random



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
ace = 1
user_score = 0
computer_score = 0

def deal_card():
    for card in random.sample(cards, len(cards)):
        cards.remove(card)
        return card
# Function deals random Cards and delete it after in the list cards[]

def start_deck():
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
# User and computer start cards

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
def calculate_score(cards):
    card_score = sum(cards)
    if len(cards) == 2:
        if card_score == 21:
            print("You have a Blackjack. You win.")
    return card_score





start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
user_finish = 0
computer_finish = 0
while start == "y":
    if not user_cards:
        start_deck()
        calculate_score(user_cards)
        print(user_cards)
        calculate_score(computer_cards)
        print(computer_cards)
        print(calculate_score(cards))