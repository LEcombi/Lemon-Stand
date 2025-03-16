import random
import time
import subprocess

Number = random.randrange(1, 100)

lemonade_Buying_Price = 0.89
Rainy = 0.76                        #Set the Conditions
Level = 1

New_Price = "False"

if Level == 1:
    Money = 100 #Set the starting money, if this the first level


Normal_Price = lemonade_Buying_Price *2.8
usury_price_1 = lemonade_Buying_Price *3.8       #Set the usury prices
usury_price_2 = lemonade_Buying_Price *4.8
usury_price_3 = lemonade_Buying_Price *5.8


RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

if Number > 50 or Number == 50:
    Weather = "Sunny"
elif Number < 50:
    Weather = "Rainy"

while True:
    Number2 = random.randrange(0, 10)
    if Number2 < 1:
        lemonade_Buying_Price *= 2
        New_Price = "True"

    if New_Price == "True":
        print("The price of the lemonade has changed!")
        print(f"The new price is {BLUE}{lemonade_Buying_Price}{RESET}")
        New_Price = "False"
    print(f"-------------------{RED}Conditions{RESET}---------------------")
    print(f"The weather is {BLUE}{Weather}{RESET} today.")
    print(f"You have {BLUE}{Money}{RESET}€")
    print(f"One lemonade costs you {RED}{lemonade_Buying_Price}{RESET}.")

    Purchasable_float = Money / lemonade_Buying_Price
    Purchasable = int(Purchasable_float)

    print(f"You can buy {BLUE}{Purchasable}{RESET} lemonades.")
    print("--------------------------------------------------")

    lemonade_Buying_Crowd = int(input("How many lemonades do you want to buy: "))

    total_cost = lemonade_Buying_Crowd * lemonade_Buying_Price
    if total_cost > Money:
        print(f"Sorry, you don't have enough money to buy {lemonade_Buying_Crowd} lemonades.")
        continue

    Money -= total_cost

    lemonade_Selling_Price = float(input("How much do you want to sell your Lemon for: "))

    if lemonade_Selling_Price - lemonade_Buying_Price < Normal_Price:
        customers = random.randrange(29, 129)
        profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers

    elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_1:
        customers = random.randrange(19, 98)
        profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers

    elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_2:
        customers = random.randrange(13, 68)
        profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers

    elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_3:
        customers = random.randrange(9, 48)
        profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers

    else:
        customers = random.randrange(1, 8)
        profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers

    if Weather == "Rainy":
        profit = profit * Rainy

    print(f"------------------{RED}Invoice{RESET}-------------------")
    print(f"You sold {BLUE}{customers}{RESET} lemonades")
    print(f"Your profit is {BLUE}{profit}{RESET}")
    print(f"That was level {BLUE}{Level}{RESET}")
    print(f"Your new account balance is {BLUE}{Money + profit}{RESET}")
    print("--------------------------------------------")

    New_Money = Money + profit
    Level = Level + 1
    Money = int(New_Money)
    time.sleep(2)