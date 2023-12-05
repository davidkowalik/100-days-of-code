import art
import random
import game_data
import os

#Functions ----------------------
def random_data():
    """This function return random item from data table."""
    return random.choice(game_data.data)

def who_won(dict_A, dict_B):
    winner = ''
    if dict_A['follower_count'] > dict_B['follower_count']:
        winner = "A"
    else:
        winner = "B"
    return winner

def print_comnpare(dict):
    print(f"Compare A: {dict['name']}, {dict['description']}, from {dict['country']}.")


# Variables -------------------
A = {}
B = {}
score = 0
lose = False

# main ----------------------
A = random_data()

while lose == False:
    os.system('cls')
    print (art.logo)
    if score != 0:
        print(f"You're right! Current score: {score}.")

    B = random_data()

    while A == B: # makeing sure taht A != B
        B = random_data()

    print(f"Compare A: {A['name']}, {A['description']}, from {A['country']}.")
    print(art.vs)
    print(f"Compare B: {B['name']}, {B['description']}, from {B['country']}.")

    vote = input("Who has more followers? Type 'A' or 'B': ")

    winner = who_won(A,B)

    if vote == winner:
        score += 1
        A = B
    else:
        lose = True
        os.system('cls')
        print (art.logo)
        print(f"Sorry, that's wrong! Final score: {score}.")
# TODO - 123091509234 


# TODO - 2 asl;dkfj ;alskjg df