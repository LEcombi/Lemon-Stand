import random
import json
import os

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = "\033[0m"

def set_weather():
    Number = random.randrange(1, 100)
    if Number > 50 or Number == 50:
        Number2 = random.randrange(1, 100)
        if Number2 < 50:
            return "Sunny"
        elif Number2 < 50:
            return "Slightly cloudy"
    elif Number < 50:
        return "Rainy"

def save_game(filename, game_state):
    with open(filename, 'w') as f:
        json.dump(game_state, f)
    print(f"Game saved to {filename}")

def load_game(filename):
    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
        print(f"Game loaded from {filename}")
        return game_state
    except FileNotFoundError:
        print(f"No saved game found with the name {filename}")
        return None

def load_game_levels(filename):
    try:
        with open(filename, 'r') as f:
            game_state = json.load(f)
        return game_state
    except FileNotFoundError:
        print(f"No saved game found with the name {filename}")
        return None

def check_exist_game(json_file_name):
    if os.path.exists(json_file_name):
        load_option = input("A saved game was found. Do you want to load it? (yes/no): ")
        if load_option.lower() == 'yes':
            loaded_game_state = load_game('game_save.json')
            if loaded_game_state:
                game_state = loaded_game_state