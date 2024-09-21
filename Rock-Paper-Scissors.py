import tkinter as tk
import random


# Function to handle user choice and determine the winner
def play(user_choice):
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    if user_choice == computer_choice:
        result.set(f"Tie! Both chose {user_choice}.")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        result.set(f"You win! {user_choice} beats {computer_choice}.")
    else:
        result.set(f"You lose! {computer_choice} beats {user_choice}.")

    score_update(user_choice, computer_choice)


# Function to update the score
def score_update(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        return
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        user_score += 1
    else:
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")


# Initialize the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors")
window.geometry("400x300")

# Variables to track scores
user_score = 0
computer_score = 0

# Display result
result = tk.StringVar()
result.set("Choose Rock, Paper, or Scissors to start the game.")

result_label = tk.Label(window, textvariable=result, font=('Helvetica', 12))
result_label.pack(pady=20)

# Buttons for user choices
rock_button = tk.Button(window, text="Rock", width=15, command=lambda: play('rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(window, text="Paper", width=15, command=lambda: play('paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(window, text="Scissors", width=15, command=lambda: play('scissors'))
scissors_button.pack(pady=5)

# Display score
score_label = tk.Label(window, text=f"Score - You: {user_score} | Computer: {computer_score}", font=('Helvetica', 12))
score_label.pack(pady=20)

# Run the main loop
window.mainloop()
