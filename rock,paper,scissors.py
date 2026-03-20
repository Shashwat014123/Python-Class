import tkinter as tk
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("500x400")

player_score = 0
computer_score = 0
score = []

choices = ["Rock", "Paper", "Scissors"]

# ADDED LABELS
computer_label = tk.Label(root, text="Computer: ")
computer_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ")
result_label.pack(pady=5)

score_label = tk.Label(root, text="Score: 0 - 0")
score_label.pack(pady=5)


def play(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(choices)
    choice = ""

    if player_choice == computer_choice:
        choice = "tie"

    elif player_choice == "Rock" and computer_choice == "Scissors":
        choice = "You win!"
        player_score += 1

    elif player_choice == "Paper" and computer_choice == "Rock":
        choice = "You win!"
        player_score += 1

    elif player_choice == "Scissors" and computer_choice == "Paper":
        choice = "You win!"
        player_score += 1
    
    else:
        choice = "You lose!"
        computer_score += 1

    # UPDATE LABELS (instead of just print)
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=f"Result: {choice}")
    score_label.config(text=f"Score: player {player_score} - computer {computer_score}")

    # keep your prints (optional)
    print(choice)
    print(f"Score: player: {player_score}, computer: {computer_score}")


rock_button = tk.Button(root, text="Rock", command=lambda: play("Rock"))
rock_button.pack(pady=10)

paper_button = tk.Button(root, text="Paper", command=lambda: play("Paper"))
paper_button.pack(pady=10)

scissors_button = tk.Button(root, text="Scissors", command=lambda: play("Scissors"))
scissors_button.pack(pady=10)

root.mainloop()