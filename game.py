print("Rock, Paper, Scissors, Shoot!")

user_choice = input("Please choose one of 'rock', 'paper', 'scissors': ")
print(user_choice)



if (user_choice == "rock") or (user_choice == "paper") or (user_choice == "scissors"):
    print("VALID. KEEP GOING")
else:
    print("OOPS, INVALID INPUT. PLEASE TRY AGAIN.")
    quit()


print("This is the end of our game! Please play again.")

# validate the input
