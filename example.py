import os
import random
import time
import sys
import threading
import collections

# --- Game Configuration ---
# Board dimensions (rows, columns)
BOARD_HEIGHT = 25
BOARD_WIDTH = 25 # Make it wider for more lanes
LANE_WIDTH = 5 # Width of each visual lane, not actual character width
NUM_LANES = BOARD_WIDTH // LANE_WIDTH # Number of logical lanes

# Player car character
PLAYER_CAR_CHAR = 'A'
# Obstacle character
OBSTACLE_CHAR = '#'

# Initial game speed (lower is faster, in seconds per frame)
INITIAL_GAME_SPEED = 0.15
# How much game speed increases (decreases time per frame) per 100 points
SPEED_INCREASE_RATE = 0.005
# Minimum game speed
MIN_GAME_SPEED = 0.05

# Obstacle spawning
OBSTACLE_SPAWN_CHANCE = 0.4 # Probability an obstacle spawns each frame (0.0 to 1.0)
MAX_OBSTACLES = 8 # Maximum obstacles on screen at once

# --- Global Game State ---
game_board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
player_x = BOARD_WIDTH // 2 # Player car's horizontal position
player_y = BOARD_HEIGHT - 2 # Player car's vertical position (near bottom)
score = 0
game_over = False
current_game_speed = INITIAL_GAME_SPEED
obstacle_count = 0 # To manage MAX_OBSTACLES

# Queue for handling non-blocking input
input_queue = collections.deque()

# --- Utility Functions ---

def clear_console():
    """Clears the console screen based on the operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_player_input():
    """Reads single character input without blocking."""
    # This function will run in a separate thread to continuously capture input
    # and add it to a queue. This allows the main game loop to continue
    # without waiting for user input.
    try:
        # For Windows
        import msvcrt
        while not game_over:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').lower()
                input_queue.append(key)
            time.sleep(0.01) # Small delay to prevent busy-waiting
    except ImportError:
        # For Unix-like systems (Linux, macOS)
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setcbreak(fd) # Set terminal to raw mode (no buffering)
            while not game_over:
                if sys.stdin.readable(): # Check if input is available
                    key = sys.stdin.read(1).lower()
                    input_queue.append(key)
                time.sleep(0.01)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # Restore terminal settings

# --- Game Logic Functions ---

def initialize_board():
    """Sets up the initial empty game board."""
    global game_board
    game_board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

def draw_board():
    """Draws the current state of the game board to the console."""
    clear_console()

    # Draw top border
    print('-' * (BOARD_WIDTH + 2))

    for r in range(BOARD_HEIGHT):
        row_str = '|'
        for c in range(BOARD_WIDTH):
            # Add road lines for better visual
            if c % LANE_WIDTH == 0 and c != 0 and r % 5 < 3: # Dashed lines every LANE_WIDTH columns
                 row_str += '|'
            else:
                row_str += game_board[r][c]
        row_str += '|'
        print(row_str)

    # Draw bottom border
    print('-' * (BOARD_WIDTH + 2))
    print(f"Score: {score} | Speed: {1/current_game_speed:.1f}x")


def place_player_car():
    """Places the player car on the board."""
    # Ensure player car stays within bounds
    global player_x
    player_x = max(0, min(player_x, BOARD_WIDTH - 1))
    game_board[player_y][player_x] = PLAYER_CAR_CHAR

def spawn_obstacle():
    """Spawns a new obstacle at a random top lane."""
    global obstacle_count
    if obstacle_count < MAX_OBSTACLES and random.random() < OBSTACLE_SPAWN_CHANCE:
        lane = random.randint(0, NUM_LANES - 1)
        # Place obstacle in the middle of a randomly chosen lane at the very top
        obstacle_x = random.randint(lane * LANE_WIDTH, (lane + 1) * LANE_WIDTH - 1)
        # Ensure obstacle_x is within bounds
        obstacle_x = max(0, min(obstacle_x, BOARD_WIDTH - 1))

        # Check if the top row already has an obstacle at this position (to avoid overlaps)
        if game_board[0][obstacle_x] == ' ':
            game_board[0][obstacle_x] = OBSTACLE_CHAR
            obstacle_count += 1

def update_obstacles():
    """Moves existing obstacles down the board."""
    global game_board, obstacle_count, game_over
    new_game_board = [[' ' for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]
    obstacles_cleared_this_frame = 0

    for r in range(BOARD_HEIGHT):
        for c in range(BOARD_WIDTH):
            if game_board[r][c] == OBSTACLE_CHAR:
                # If obstacle is at the bottom, it's cleared
                if r + 1 >= BOARD_HEIGHT:
                    obstacles_cleared_this_frame += 1
                else:
                    new_game_board[r + 1][c] = OBSTACLE_CHAR
    game_board = new_game_board
    obstacle_count -= obstacles_cleared_this_frame


def check_collisions():
    """Checks for collisions between player car and obstacles."""
    global game_over
    if game_board[player_y][player_x] == OBSTACLE_CHAR:
        game_over = True

def update_game_speed():
    """Adjusts the game speed based on the score."""
    global current_game_speed
    speed_increase = (score // 100) * SPEED_INCREASE_RATE
    current_game_speed = max(MIN_GAME_SPEED, INITIAL_GAME_SPEED - speed_increase)

# --- Main Game Loop ---

def game_loop():
    """The main loop of the car running game."""
    global player_x, score, game_over

    input_thread = threading.Thread(target=get_player_input, daemon=True)
    input_thread.start()

    while not game_over:
        initialize_board() # Clear board for redraw

        # Handle player input from queue
        while input_queue:
            key = input_queue.popleft()
            if key == 'a' or key == 'arrowleft':
                player_x -= 1
            elif key == 'd' or key == 'arrowright':
                player_x += 1
            # Ensure player car stays within bounds after movement
            player_x = max(0, min(player_x, BOARD_WIDTH - 1))

        # Place player car on the updated board
        place_player_car()

        # Update and move obstacles
        update_obstacles()
        spawn_obstacle()

        # Check for collisions after moving obstacles and before drawing
        check_collisions()

        # If game is over, break loop before drawing a final time
        if game_over:
            break

        # Draw everything
        draw_board()

        # Update score
        score += 1

        # Adjust game speed
        update_game_speed()

        # Wait for the next frame
        time.sleep(current_game_speed)

    # Game Over screen
    clear_console()
    print("-" * (BOARD_WIDTH + 2))
    print(f"|{' ' * BOARD_WIDTH}|")
    print(f"|{' ' * ((BOARD_WIDTH - 9) // 2)}GAME OVER{' ' * ((BOARD_WIDTH - 9) // 2)}{' ' if BOARD_WIDTH % 2 != 0 else ''}|")
    print(f"|{' ' * BOARD_WIDTH}|")
    print(f"|{' ' * ((BOARD_WIDTH - len(f'Final Score: {score}')) // 2)}Final Score: {score}{' ' * ((BOARD_WIDTH - len(f'Final Score: {score}')) // 2)}{' ' if (BOARD_WIDTH - len(f'Final Score: {score}')) % 2 != 0 else ''}|")
    print(f"|{' ' * BOARD_WIDTH}|")
    print("-" * (BOARD_WIDTH + 2))
    print("\nPress Ctrl+C to exit.")


# --- Start the Game ---
if __name__ == "__main__":
    try:
        game_loop()
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nExiting game.")

