import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x400")

player_score = 0
computer_score = 0
score = []

choices = ["Rock", "Paper", "Scissors"]


def play(player_choice):
    computer_choice = random.choice(choices)
    choice = ""

    if player_choice == computer_choice:
        choice = "tie"
        print(choice)
        print(f"Score: player: {player_score}, computer: {computer_score}")

    elif player_choice == "Rock" and computer_choice == "Scissors":
        choice = "You win!"
        player_score += 1
        print(choice)
        print(f"Score: player: {player_score}, computer: {computer_score}")

    elif player_choice == "Paper" and computer_choice == "Rock":
        choice = "You win!"
        player_score += 1
        print(choice)
        print(f"Score: player: {player_score}, computer: {computer_score}")

    elif player_choice == "Scissors" and computer_choice == "Paper":
        choice = "You win!"
        player_score += 1
        print(choice)
        print(f"Score: player: {player_score}, computer: {computer_score}")
    
    else:
        choice = "You lose!"
        computer_score += 1
        print(choice)
        print(f"Score: player: {player_score}, computer: {computer_score}")

rock_button = tk.Button(root, text="Rock", command=play("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=play("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=play("Scissors"))
scissors_button.pack(pady=10)

root.mainloop()