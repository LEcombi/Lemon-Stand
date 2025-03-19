from storage import load_game_levels, save_game
from Game import Invoice
from storage import RED, BLUE, RESET
import random
import time

game_state = load_game_levels('../game_save.json')


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
            customers = random.randrange(39, 169)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(29, 122)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(22, 82)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(16, 72)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(3, 13)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    if game_state['Weather'] == "Slightly cloudy":
        if lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['Normal_Price']:
            customers = random.randrange(35, 201)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(26, 152)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(19, 122)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(11, 85)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(3, 13)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    if game_state['Weather'] == "Rainy":
        if lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['Normal_Price']:
            customers = random.randrange(19, 54)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_1']:
            customers = random.randrange(9, 74)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_2']:
            customers = random.randrange(8, 58)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        elif lemonade_Selling_Price - game_state['lemonade_Buying_Price'] < game_state['usury_price_3']:
            customers = random.randrange(7, 38)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

        else:
            customers = random.randrange(4, 19)
            profit = (lemonade_Selling_Price - game_state['lemonade_Buying_Price']) * customers

    New_Money = game_state['Money'] + profit

    profit =None
    Invoice(customers, profit, New_Money, game_state)

    game_state['Level'] += 1
    game_state['Money'] = int(New_Money)
    time.sleep(2)

    # Save game after each level
    save_game('game_save.json', game_state)
