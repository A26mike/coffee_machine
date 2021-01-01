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

money = 0.00

resources = {
    "water": 5,
    "milk": 200,
    "coffee": 100,
}

def print_resources():
        print(f"""
            Water:  {resources["water"]}
            Milk:   {resources["milk"]}    
            Coffee: {resources["coffee"]} 
            money:  {money:.2f}  
         """)

# Check if resources are sufficient to make chcoic returns false if unable to make 
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
        return True 

def calculate_cash(drink_choice):
    total = 0
    cost = MENU[drink_choice]["cost"]
    print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} please insert enter exact amount')

    dollars = int(input('Please insert dollars if none enter 0:  '))
    if dollars > 0:
        total += dollars * 1.00
        remaining = cost - total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')

    quarters = int(input('Please insert quarters if none enter 0:  '))
    if quarters > 0:
        total += quarters * 0.25
        remaining = cost - total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')

    dimes = int(input('Please insert dimes if none enter 0:  '))
    if dimes > 0:
        total += dollars * 0.10
        remaining = cost -total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')

    nickles = int(input('Please insert nickles if none enter 0:  '))
    if nickles > 0:
        total += nickles * 0.05
        remaining = cost -total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')

    pennies = int(input('Please insert pennies if none enter 0:  '))
    if pennies > 0:
        total += pennies * 0.01
        remaining = cost -total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')
    
    return total


def ammount_correct(inserted,expected):
    if inserted == expected:
        print("Transaction successful amount correct")
        global money 
        money += expected
        return True
    
    elif inserted < expected:
        print("Sorry that's not enough money. {inserted} refunded.")
        return False

    elif inserted > expected:
        global money
        refund = inserted - expected
        money += expected
        print("Transaction successful. “Here is ${refund} dollars in change.")
        return True

#TODO Make Coffee.
def make_coffee():
    pass


# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# money: $2.5


#TODO If there are sufficient resources to make the drink selected, then the program should





#define main loop

menu_choice = input('What would you like? (espresso/latte/cappuccino):')
print('\n')

test = calculate_cash(menu_choice)

if menu_choice == "report":
    pass

print(f'test:.2f')

#resource_checker(menu_choice)
