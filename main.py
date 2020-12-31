MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

MONEY = 0.00

resources = {
    "water": 5,
    "milk": 200,
    "coffee": 100,
}


def print_resources:
        print(f"""
            Water:  {resources["water"]}
            Milk:   {resources["milk"]}    
            Coffee: {resources["coffee"]} 
            Money:  {money:.2f}  
         """)

#TODO make better logic for resource checker 

# Check if resources sufficient
def resource_checker(choice):
    if resources["water"] < MENU[choice]["ingredients"]["water"]:
        print(f"""
                Sorry there is only {resources["water"]}ml of water remaining in the machine,
                unfortunately your choice of {choice} requires {MENU[choice]["ingredients"]["water"]}ml of water.            
                """)
        return False

    elif resources["coffee"] < MENU[choice]["ingredients"]["coffee"]:
        print(f"""
                Sorry there is only {resources["coffee"]}g of coffee remaining in the machine,
                unfortunately your choice of {choice} requires {MENU[choice]["ingredients"]["coffee"]}g of coffee.            
                """)
        return False
    elif resources["milk"] < MENU[choice]["ingredients"]["milk"]:
        print(f"""
                Sorry there is only {resources["milk"]}ml milk remaining in the machine,
                unfortunately your choice of {choice} requires {MENU[choice]["ingredients"]["milk"]}ml of milk.            
        """)
        return False
    else:
        return true 

 #TODO Process coins.

# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

#TODO Check transaction successful?

# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

#TODO Make Coffee.

# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5



#define main loop

menu_choice = input('What would you like? (espresso/latte/cappuccino):')


if menu_choice == "report":


resource_checker(menu_choice)
