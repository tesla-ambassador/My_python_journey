from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_maker = MoneyMachine()

def make_the_coffee():
    should_continue = True
    while should_continue:
        choice = input('What would you like to drink? ')
        if choice in menu.get_items():
            drink = menu.find_drink(choice)
            if coffee_machine.is_resource_sufficient(drink):
                money_maker.make_payment(drink.cost)
                coffee_machine.make_coffee(drink)
        elif choice == 'report':
            coffee_machine.report()
            money_maker.report()
        elif choice == 'off':
            should_continue == False
            return
        else:
            print('Invalid Choice')
            return

make_the_coffee()