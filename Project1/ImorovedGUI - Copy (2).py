import tkinter as tk
import random

# Constants
SNAKE = 1
WATER = -1
GUN = 0

choices = {"snake": SNAKE, "water": WATER, "gun": GUN}
reverse_map = {SNAKE: "Snake", WATER: "Water", GUN: "Gun"}
winning_cases = {
    (SNAKE, WATER): "win",  # Snake drinks water
    (WATER, GUN): "win",    # Water drowns gun
    (GUN, SNAKE): "win",    # Gun kills snake
}

# Score variables
user_score = 0
computer_score = 0

# Game Logic Function
def play(user_choice):
    global user_score, computer_score
    user = choices[user_choice]
    computer = random.choice([SNAKE, WATER, GUN])

    user_choice_label.config(text=f"You chose: {reverse_map[user]}")
    computer_choice_label.config(text=f"Computer chose: {reverse_map[computer]}")

    if user == computer:
        result_label.config(text="🤝 It's a draw!", fg="orange")
    elif (user, computer) in winning_cases:
        result_label.config(text="🎉 You win!", fg="green")
        user_score += 1
    else:
        result_label.config(text="😢 You lose!", fg="red")
        computer_score += 1

    score_label.config(text=f"Score - You: {user_score} | Computer: {computer_score}")

# Reset Game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Score - You: 0 | Computer: 0")

# GUI Setup
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("420x350")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Button Frame
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Snake", width=10, command=lambda: play("snake")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water", width=10, command=lambda: play("water")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun", width=10, command=lambda: play("gun")).grid(row=0, column=2, padx=5)

# Output Labels
user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

# Control Buttons
control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="Exit", width=10, command=root.quit).grid(row=0, column=1, padx=10)

# Start GUI Loop
root.mainloop()
