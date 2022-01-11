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
}


def print_report():
    """ prints report listing resources needed to make coffee and how much money is in the machine. """
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: ${money_in_machine}")


def has_sufficient_resources(drink):
    """ returns True if enough resources in coffee machine to make the drink, false otherwise """
    for k in drink['ingredients']:
        if resources[k] < drink['ingredients'][k]:
            print(f"Sorry there is not enough {k}.")
            return False
    return True


def process_coins():
    """ returns the total of coins inserted """
    print("Please insert coins.")
    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickles = int(input("How many nickles? "))
    num_pennies = int(input("How many pennies? "))
    return num_quarters * .25 + num_dimes * .10 + num_nickles * .05 + num_pennies * .01


def make_coffee(ingredients):
    """ adjusts resources in machine based on how much required to make this drink """
    for k in ingredients:
        resources[k] -= ingredients[k]


def process_drink (drink_type):
    global money_in_machine

    requested_drink = MENU[drink_type]
    if has_sufficient_resources(requested_drink):
        money_paid = process_coins()
        change = round(money_paid - requested_drink['cost'], 2)
        if change >= 0:
            make_coffee(requested_drink['ingredients'])
            money_in_machine += requested_drink['cost']
            print(f'Your change is ${change:.2f}. Enjoy your {drink_type.title()} ☕')
        else:
            print("Sorry, that is not enough money. Money refunded.")


machine_on: bool = True
money_in_machine: float = 0.0
while machine_on:
    user_input = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "report":
        print_report()
    elif user_input == "off":
        machine_on = False
    elif user_input in MENU:
        process_drink(user_input)


