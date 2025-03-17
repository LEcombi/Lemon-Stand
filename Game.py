
import time
from storage import *

# Initial game state
game_state = {
    'lemonade_Buying_Price': 0.89,
    'Rainy': 0.76,
    'Level': 1,
    'Money': 100,
    'complete_usury': 10,
    'Normal_Price': 0.89 * 2.8,
    'usury_price_1': 0.89 * 3.8,
    'usury_price_2': 0.89 * 4.8,
    'usury_price_3': 0.89 * 5.8,
    'Price_per_advertising_sign': 15,
    'New_Price': "False",
    'Weather': set_weather()
}


RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
RESET = "\033[0m"

check_exist_game("game_save.json")

while True:
    Number2 = random.randrange(0, 10)
    if Number2 < 1:
        game_state['lemonade_Buying_Price'] *= 2
        game_state['New_Price'] = "True"
        game_state['usury_price_1'] = game_state['lemonade_Buying_Price'] * 3.8
        game_state['Normal_Price'] = game_state['lemonade_Buying_Price'] * 2.8
        game_state['usury_price_2'] = game_state['lemonade_Buying_Price'] * 4.8
        game_state['usury_price_3'] = game_state['lemonade_Buying_Price'] * 4.8

    if game_state['New_Price'] == "True":
        print("The price of the lemonade has changed!")
        print(f"The new price is {BLUE}{game_state['lemonade_Buying_Price']}{RESET}")
        game_state['New_Price'] = "False"

    print(f"-------------------{RED}Conditions{RESET}---------------------")
    print(f"The weather is {BLUE}{game_state['Weather']}{RESET} today.")
    print(f"You have {BLUE}{game_state['Money']}{RESET}€")
    print(f"One lemonade costs you {RED}{game_state['lemonade_Buying_Price']}{RESET}.")

    Purchasable_float = game_state['Money'] / game_state['lemonade_Buying_Price']
    Purchasable = int(Purchasable_float)

    print(f"You can buy {BLUE}{Purchasable}{RESET} lemonades.")
    print("--------------------------------------------------")
    try:
        lemonade_Buying_Crowd = int(input("How many lemonades do you want to buy: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    total_cost = lemonade_Buying_Crowd * game_state['lemonade_Buying_Price']
    if total_cost > game_state['Money']:
        print(f"Sorry, you don't have enough money to buy {lemonade_Buying_Crowd} lemonades.")
        continue

    game_state['Money'] -= total_cost
    try:
        lemonade_Selling_Price = float(input("How much do you want to sell your Lemon for: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if lemonade_Selling_Price < game_state['complete_usury'] or lemonade_Selling_Price == game_state['complete_usury']:
        customers = 0
        profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    if game_state['Weather'] == "Sunny":
        if lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['Normal_Price']:
            customers = random.randrange(29, 129)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(19, 98)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(13, 68)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(9, 48)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(1, 8)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    if game_state['Weather'] == "Slightly cloudy":
        if lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['Normal_Price']:
            customers = random.randrange(25, 176)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(15, 122)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(9, 102)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(5, 65)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(1, 12)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    if game_state['Weather'] == "Rainy":
        if lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['Normal_Price']:
            customers = random.randrange(15, 68)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(5, 48)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(3, 38)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(1, 28)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(1, 8)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    New_Money = game_state['Money'] + profit
    profit =None

    print(f"------------------{RED}Invoice{RESET}-------------------")
    print(f"You sold {BLUE}{customers}{RESET} lemonades")
    print(f"Your profit is {BLUE}{profit}{RESET}")
    print(f"That was level {BLUE}{game_state['Level']}{RESET}")
    print(f"Your new account balance is {BLUE}{New_Money}{RESET}")
    print("--------------------------------------------")

    game_state['Level'] += 1
    game_state['Money'] = int(New_Money)
    time.sleep(2)

    # Save game after each level
    save_game('game_save.json', game_state)