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

print("Welcome "+ PLAYER_NAME + " to Rock, Paper, Scissors, Shoot!")
user_choice = input("Please choose one of the following: 'rock', 'paper', or 'scissors'.")

if user_choice = "rock" or "paper" or "scissors":
        print("Valid, keep going!")
else:
        print("Oops, that's not an option. Please try again.")
        exit()
print("This is the end of our game. Please play again.")

print("USER CHOICE: ", user_choice)
if user_choice == computer_choice:
    print("It's a tie, try again!")
elif (user_choice == "scissors") and (computer_choice == "paper"):
        print("Scissors cuts paper, you win!")
elif (user_choice == "rock") and (computer_choice == "scissors"):
        print("rock smashes scissors, you win!")
elif (user_choice == "paper") and (computer_choice == "rock"):
        print("Paper covers rock, you win!")
#COMPUTER WINNING SCENARIOS
elif (user_choice == "scissors") and (computer_choice == "rock"):
        print("rock smashes scissors, you lose!")
elif (user_choice == "rock") and (computer_choice == "paper"):
        print("paper covers rock, you lose!")
elif (user_choice == "paper") and (computer_choice == "scissors"):
        print("Scissors cuts paper, you lose!")

exit()
print("Thank you for playing!")