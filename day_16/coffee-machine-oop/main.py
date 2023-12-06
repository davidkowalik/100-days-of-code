from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

off = False

while not off:
    choice = input(f"What would you like? ({menu.get_items()}): ")
    if choice == "report":
        coffeemaker.report()
        money.report()
    elif choice == "off":
        off = True
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
