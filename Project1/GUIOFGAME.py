import tkinter as tk
import random

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


def play(user_choice):
    user = choices[user_choice]
    computer = random.choice([SNAKE, WATER, GUN])

    user_choice_label.config(text=f"You chose: {reverse_map[user]}")
    computer_choice_label.config(text=f"Computer chose: {reverse_map[computer]}")

    if user == computer:
        result_label.config(text="🤝 It's a draw!", fg="orange")
    elif (user, computer) in winning_cases:
        result_label.config(text="🎉 You win!", fg="green")
    else:
        result_label.config(text="😢 You lose!", fg="red")


root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("400x300")
root.resizable(False, False)


title_label = tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

# Buttons
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

# Exit Button
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

# Start GUI Loop
root.mainloop()
