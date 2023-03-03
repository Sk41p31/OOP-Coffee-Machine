from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
import os


my_menu = Menu()
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()

continue_machine = True

while continue_machine:


    print(logo)

    user_decision = input(f"Please select your drink: {my_menu.get_items()}: ")
    if user_decision == 'report':
        my_coffee_machine.report()
        my_money_machine.report()
    elif user_decision == 'off':
        continue_machine = False
    else:
        chosen_drink = my_menu.find_drink(user_decision)
        if chosen_drink is None:
            print("\nWrong choice! Try again!")
        else:
            if my_coffee_machine.is_resource_sufficient(chosen_drink):
                enough_money = my_money_machine.make_payment(chosen_drink.cost)
                while not enough_money:
                    enough_money = my_money_machine.make_payment(chosen_drink.cost)
                my_coffee_machine.make_coffee(chosen_drink)

    print("\n" * 5)