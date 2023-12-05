import os

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

choice: str = ""
OFF = False


# functions definitions ----------------
def print_report(rss):
    """Print resources report"""
    print(f"Water: {rss['water']}ml")
    print(f"Milk: {rss['milk']}ml")
    print(f"Coffee: {rss['coffee']}g")
    print(f"Money: ${rss['money']}")

def check_rss(drink, rss):
    output = True
    for item in drink["ingredients"]:
        if drink["ingredients"][item] > rss[item]:
            output = False
            print(f"Sorry there is not enough {item}")
    return output

def process_coins(drink):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    money = round(quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01, 4)
    print(money)
    if money >= drink["cost"]:
        resources["money"] += drink["cost"]
        print(f"Here is ${round(money - drink['cost'], 4)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def brew_coffee(drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]

# TODO: 1 - print report - resources - DONE
# TODO: 2 - check if You have enough resources - DONE
# TODO: 3 - Implement turn OFF - DONE
# TODO: 4 - Implement process coins


os.system('cls')

while not OFF:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print_report(resources)
    elif choice == "off":
        OFF = True
    else:
        if check_rss(MENU[choice], resources):
            if process_coins(MENU[choice]):
                brew_coffee(MENU[choice])
                print(f"Here is your {choice} ☕️. Enjoy!")
