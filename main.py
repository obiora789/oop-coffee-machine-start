from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu = Menu()
menu_item = MenuItem("name", "water", "milk", "coffee", "cost")
make_coffee = CoffeeMaker()
coin_bank = MoneyMachine()

on = True
while on:
    user_order = input(f"What would you like? {menu.get_items()}: ")
    if user_order == "off":
        print("GoodBye!")
        on = False
    elif user_order == "report":
        make_coffee.report()
        coin_bank.report()
    elif user_order == "restock":
        make_coffee.restock_resources()
    else:
        drink = menu.find_drink(user_order)
        if make_coffee.is_resource_sufficient(drink) and coin_bank.make_payment(drink.cost):
            make_coffee.make_coffee(drink)
