import random

Number = random.randrange(1, 100)
lemonade_Buying_Price = 0.89

usury_price_1 = 3.50
usury_price_2 = 4.50
usury_price_3 = 5.50
Normal_Price = 2.50

RED = "\033[31m"
RESET = "\033[0m"

if Number > 50 or Number == 50:
    Weather = "Sunny"
elif Number < 50:                 #Set the weather
    Weather = "Rainy"

print(f"The weather is {Weather} today.")
print(f"One lemonade costs you {RED}{lemonade_Buying_Price}{RESET}.")
lemonade_Selling_Price = float(input("How much do you want to sell your Lemon for: "))


if lemonade_Selling_Price - lemonade_Buying_Price < Normal_Price:
    customers = random.randrange(29, 129)
    profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers
    print(profit)

elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_1:
    customers = random.randrange(19, 98)
    profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers
    print(profit)

elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_2:
    customers = random.randrange(13, 68)
    profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers
    print(profit)

elif lemonade_Selling_Price - lemonade_Buying_Price < usury_price_3:
    customers = random.randrange(9, 48)
    profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers
    print(profit)
else:
    customers = random.randrange(3, 28)
    profit = (float(lemonade_Selling_Price) - lemonade_Buying_Price) * customers
    print(profit)



