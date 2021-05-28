# game.py
import random
import os
from dotenv import load_dotenv

load_dotenv()


PLAYER_NAME = os.getenv("PLAYER_NAME")

print(PLAYER_NAME)

option = ['rock', 'paper', 'scissors']
print(random.choice(option))
computer_choice = random.choice(option)

print("Welcome, "+ PLAYER_NAME + " to Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose one of the following: 'rock', 'paper', or 'scissors'.")

print(user_choice)

#USER WINNING SCENARIOS
if user_choice == computer_choice:
    print("It's a tie, try again!")
elif (user_choice == "scissors") and (computer_choice == "paper"):
        print("Scissors cut paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
        print("Rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
        print("Paper covers rock, you win!")

#COMPUTER WINNING SCENARIOS
elif (user_choice == "scissors") and (computer_choice == "rock"):
        print("Rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
        print("Paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
        print("Scissors cut paper, you lose!")
else:
        print("Oops, that's not an option. Please play again.")
        exit()