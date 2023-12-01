from resource import MENU
from resource import resources
from resource import coins

product = ""
machine_status = True

def off():
    print("Coffee machine shut down. Please wait.")
    machine_status = False
    return machine_status

def report():
    print(f"water: ", resources["water"],"\nmilk: ", resources["milk"], "\ncoffee: ", resources["coffee"],"\nMoney: ", resources["money"])

def user_product():
    product = MENU[user_choice]["ingredients"]
    return product

def check_inventory():
    inventory = True
    for ingredients in user_product():
        if resources[ingredients] < user_product()[ingredients]:
            print(f"Sorry there is not enough", ingredients, ".")
            inventory = False
    return inventory

def calculating_resources():
    for ingredients in user_product():
        resources[ingredients] = resources[ingredients] - user_product()[ingredients]

def payed():
    user_payed_correct = False
    while user_payed_correct == False:
        print(f"Please insert $",MENU[user_choice]["cost"])
        abort = input("To abort the process press 'n' or to continue 'y'. ")
        if abort == "y":
            payed_quarters = int(input("How many quarters? ")) * float(coins["quarters"])
            payed_dimes = int(input("How many dimes? ")) * float(coins["dimes"])
            payed_nickles = int(input("How many nickles? ")) * float(coins["nickles"])
            payed_pennies = int(input("How many pennies? ")) * float(coins["pennies"])
            user_payed = payed_quarters + payed_dimes + payed_nickles + payed_pennies
            if MENU[user_choice]["cost"] == float(user_payed):
                resources["money"] = resources["money"] + user_payed
                print("Thank you for your payment.")
                user_payed_correct = True
                return user_payed_correct
            elif float(MENU[user_choice]["cost"]) < float(user_payed):
                payback = float(user_payed) - MENU[user_choice]["cost"]
                resources["money"] += (user_payed - payback)
                print(f"You payed to much. You become $",payback ,"back. Thank you for your payment.")
                user_payed_correct = True
                return user_payed_correct
            else:
                print("You payed not enough for this product.")
        else:
            break

while machine_status:
    user_choice = input(f"\nOptions are:\nespresso $1.50\nlatte $2.50\ncappucciono $3.00\nreport\noff\nWhat would you like?\n")
    if user_choice == "off":
        machine_status = off()
    elif user_choice == "report":
        report()
    elif user_choice in ["espresso", "latte", "cappuccino"]:
        if check_inventory() == True:
            if payed() == True:
                calculating_resources()
                print(f"Process product. Please wait.\nHere is your",user_choice,". Enjoy!")
    else:
        print("Your input can't be execute. Please try again.")
