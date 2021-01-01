

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
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

    elif choice == "latte" or choice == "cappuccino" :
        if resources["milk"] < MENU[choice]["ingredients"]["milk"]:
            print(f"""
Sorry there is only {resources["milk"]}ml milk remaining in the machine,
unfortunately your choice of {choice} requires {MENU[choice]["ingredients"]["milk"]}ml of milk.            
            """)
            return False
        return True
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
        if total >= cost:
            return total

    quarters = int(input('Please insert quarters if none enter 0:  '))
    if quarters > 0:
        total += quarters * 0.25
        remaining = cost - total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')
        if total >= cost:
            return total

    dimes = int(input('Please insert dimes if none enter 0:  '))
    if dimes > 0:
        total += dimes * 0.10
        remaining = cost -total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')
        if total >= cost:
            return total

    nickles = int(input('Please insert nickles if none enter 0:  '))
    if nickles > 0:
        total += nickles * 0.05
        remaining = cost -total
        print(f'Your drink costs {MENU[drink_choice]["cost"]:.2f} you have ${remaining:.2f} remaining \n')
        if total >= cost:
            return total

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
        print(f"Sorry that's not enough money. {inserted} refunded.")
        return False

    elif inserted > expected:
        refund = inserted - expected
        money += expected
        print(f"Transaction successful. “Here is ${refund} dollars in change.")
        return True

def make_coffee(drink_choice):
    print('\n')
    water_used = MENU[drink_choice]["ingredients"]["water"]
    coffee_used = MENU[drink_choice]["ingredients"]["coffee"]
    Milk_used = 0
    print('Prior to making coffee')
    print_report()
    print('\n')

    if drink_choice == "latte" or drink_choice == "cappuccino" :
        Milk_used = MENU[drink_choice]["ingredients"]["milk"]
    
    resources["water"] -= water_used
    resources["coffee"] -= coffee_used
    resources["milk"] -= Milk_used
    print('After making coffee')
    print_report()
    print('\n')

#main loop 

make_drink = True
while make_drink == True:
    print('\n\n')
    menu_choice = input('What would you like? (espresso/latte/cappuccino):')
    expected_cost = MENU[menu_choice]["cost"]

    if menu_choice == "report":
        print_report()
        print('\n')
   
    elif menu_choice == "espresso" or menu_choice == "latte" or menu_choice == "cappuccino":
        print("here")
        enough_resources = resource_checker(menu_choice)

        if enough_resources == True:
            print('\n')
            inserted_cash = calculate_cash(menu_choice)
            correct_amount = ammount_correct(inserted_cash,expected_cost)

            if correct_amount == True:
                make_coffee(menu_choice)
        
    else:
        print('you have entered and incorrect menu item try again')

    make_another_drink = input("Would you like another drink ? press y to order a new drink  or press any key to quit ")
    if make_another_drink == 'y':
        make_drink = True 
    else:
        make_drink = False 
          


#TODO try and except statments 