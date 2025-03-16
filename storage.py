import random
import json
import os

def set_weather():
    Number = random.randrange(1, 100)
    if Number > 33 or Number == 33:
        return "Sunny"
    elif Number < 33:
        return "slightly cloudy"
    elif Number < 66:
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

def check_exist_game():
    if os.path.exists('game_save.json'):
        load_option = input("A saved game was found. Do you want to load it? (yes/no): ")
        if load_option.lower() == 'yes':
            loaded_game_state = load_game('game_save.json')
            if loaded_game_state:
                game_state = loaded_game_state