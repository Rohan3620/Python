import tkinter as tk
import random
import winsound

# Constants for game logic
SNAKE = 1
WATER = -1
GUN = 0

choices = {"snake": SNAKE, "water": WATER, "gun": GUN}
reverse_map = {SNAKE: "Snake 🐍", WATER: "Water 💧", GUN: "Gun 🔫"}
winning_cases = {
    (SNAKE, WATER): "win",   # Snake drinks water
    (WATER, GUN): "win",     # Water drowns gun
    (GUN, SNAKE): "win",     # Gun kills snake
}

# Score and round trackers
user_score = 0
computer_score = 0
rounds_played = 0
max_rounds = 5

# GUI setup
root = tk.Tk()
root.title("Snake 🐍 Water 💧 Gun 🔫")
root.geometry("460x380")
root.resizable(False, False)

# Play sounds based on result
def play_sound(result):
    if result == "win":
        winsound.Beep(800, 200)
    elif result == "lose":
        winsound.Beep(400, 200)
    elif result == "draw":
        winsound.Beep(600, 200)

# Flash background briefly
def flash_result(color):
    original_color = root.cget("bg")
    root.config(bg=color)
    root.after(200, lambda: root.config(bg=original_color))

# Main game logic
def play(user_choice):
    global user_score, computer_score, rounds_played

    if rounds_played >= max_rounds:
        result_label.config(text="🎯 Game over! Reset to play again.", fg="blue")
        return

    user = choices[user_choice]
    computer = random.choice([SNAKE, WATER, GUN])

    user_choice_label.config(text=f"You chose: {reverse_map[user]}")
    computer_choice_label.config(text=f"Computer chose: {reverse_map[computer]}")

    # Outcome determination
    if user == computer:
        result = "draw"
        result_label.config(text="🤝 It's a draw!", fg="orange")
    elif (user, computer) in winning_cases:
        result = "win"
        user_score += 1
        result_label.config(text="🎉 You win this round!", fg="green")
    else:
        result = "lose"
        computer_score += 1
        result_label.config(text="😢 You lose this round!", fg="red")

    play_sound(result)
    flash_result("lightgreen" if result == "win" else "lightcoral" if result == "lose" else "lightyellow")

    rounds_played += 1
    score_label.config(text=f"Round {rounds_played}/{max_rounds} | You: {user_score} | Computer: {computer_score}")

    # Final result check
    if rounds_played == max_rounds:
        if user_score > computer_score:
            result_label.config(text="🏆 You won the game!", fg="green")
        elif user_score < computer_score:
            result_label.config(text="💀 Computer wins the game!", fg="red")
        else:
            result_label.config(text="⚖️ It's a tie game!", fg="orange")

# Reset game function
def reset_game():
    global user_score, computer_score, rounds_played
    user_score = 0
    computer_score = 0
    rounds_played = 0
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text="Round 0/5 | You: 0 | Computer: 0")
    root.config(bg="SystemButtonFace")

# UI Elements
title_label = tk.Label(root, text="Snake 🐍 Water 💧 Gun 🔫", font=("Arial", 18, "bold"))
title_label.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Snake", width=10, command=lambda: play("snake")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Water", width=10, command=lambda: play("water")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Gun", width=10, command=lambda: play("gun")).grid(row=0, column=2, padx=5)

user_choice_label = tk.Label(root, text="", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = tk.Label(root, text="", font=("Arial", 12))
computer_choice_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Round 0/5 | You: 0 | Computer: 0", font=("Arial", 12))
score_label.pack(pady=5)

control_frame = tk.Frame(root)
control_frame.pack(pady=10)

tk.Button(control_frame, text="Reset", width=10, command=reset_game).grid(row=0, column=0, padx=10)
tk.Button(control_frame, text="Exit", width=10, command=root.quit).grid(row=0, column=1, padx=10)

# Start the GUI loop
root.mainloop()
