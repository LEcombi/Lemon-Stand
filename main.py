import random
from turtledemo.chaos import jumpto
import time

Number = random.randrange(1, 100)
lemonade_Buying_Price = 0.89
Rainy = 0.76

usury_price_1 = 3.50
usury_price_2 = 4.50
usury_price_3 = 5.50
Normal_Price = 2.50

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

if Number > 50 or Number == 50:
    Weather = "Sunny"
elif Number < 50:                 #Set the weather
    Weather = "Rainy"

while True:

    print(f"The weather is {Weather} today.")
    print(f"One lemonade costs you {RED}{lemonade_Buying_Price}{RESET}.")
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

    print("--------------------------------")
    print(f"You sold {BLUE}{customers}{RESET} lemonades")
    print(f"Your profit is {BLUE}{profit}{RESET}")
    print("--------------------------------")
    time.sleep(2)




