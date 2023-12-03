import os
import random

os.system('cls')

def random_number():
    """Return random number form 1 to 100 range"""
    return random.randint(1, 100)

easy = 10
hard = 5

attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")


if difficulty == 'hard':
    attempts = hard
elif difficulty == 'easy':
    attempts = easy

number = random_number()

while attempts > 0:
    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it!! the answer was {number}.")
        attempts = 0
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess < number:
        print("Too low.")
        print("Guess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

if attempts == 0:
    print("You've run out of guesses, You lose.")