import numpy as np

options = ["Rock", "Paper", "Scissors"]
computer_points = 0
player_points = 0


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "Tie"
    elif (
            (player_choice == "Rock" and computer_choice == "Scissors") or
            (player_choice == "Scissors" and computer_choice == "Paper") or
            (player_choice == "Paper" and computer_choice == "Rock")
    ):
        return "Player"
    else:
        return "Computer"


while computer_points < 2 and player_points < 2:
    player_answer = input("Rock, Paper, or Scissors? ")
    if player_answer not in options:
        print("Invalid choice. Please enter 'Rock', 'Paper', or 'Scissors'.")
        continue

    computer_answer = np.random.choice(options, size=1)
    computer_answer = computer_answer.item()

    print(f"The Computer selected {computer_answer}")
    winner = determine_winner(player_answer, computer_answer)

    if winner == "Player":
        print("Player gets a point")
        player_points += 1
    elif winner == "Computer":
        print("Computer gets a point")
        computer_points += 1
    else:
        print("It's a tie!")

if player_points > computer_points:
    print("Player Wins.")
else:
    print("Computer Wins.")
