import random

def play():
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return play()  # Restart if invalid input

    print(f"\nYou chose {user_choice}, and the computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")

# Run the game
play()
