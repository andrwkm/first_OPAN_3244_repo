
#ASK USER FOR AN INPUT (ROCK, PAPER, SCISSORS)
user_choice = input("Enter your choice (rock, paper, scissors): ")
print(f"You chose: {user_choice}")

#VALIDATIONS
valid_choices = ["rock", "paper", "scissors"]
if user_choice.lower() not in valid_choices:
    print("Invalid choice. Please choose rock, paper, or scissors.")
    exit()

#GENERATE RANDOM COMPUTER CHOICE
import random
computer_choice = random.choice(valid_choices)
print(f"Computer chose: {computer_choice}")


#DETERMINE WINNER
if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")