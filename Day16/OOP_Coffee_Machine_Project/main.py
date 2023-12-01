from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()
machine_status = True

while machine_status:
    # print(f"\nWhat would you like?",menu.get_items())
    user_choice = input(f"\nWhat would you like? ({menu.get_items()})")
    item_list = menu.get_items().split("/")
    if user_choice == "off":
        machine_status = False
    elif user_choice == "report":
        coffeemaker.report()
        moneymachine.report()
    elif user_choice in item_list:
        ordered_drink = menu.find_drink(user_choice)
        if coffeemaker.is_resource_sufficient(ordered_drink) is True:
            print(f"Please pay $", ordered_drink.cost)
            payment = moneymachine.make_payment(ordered_drink.cost)
            if payment is True:
                coffeemaker.make_coffee(ordered_drink)
    else:
        menu.find_drink(user_choice)