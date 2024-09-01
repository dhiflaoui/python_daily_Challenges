import time

coffee = 100
milk = 500
water = 300
money = 0


def coffee_needs(coffee_type):
    """Returns the resource requirements and cost for the specified coffee type."""
    return {
        "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
        "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
        "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0},
    }.get(coffee_type.lower(), None)


def check_resources(coffee_type):
    """Checks if there are sufficient resources to make the specified coffee type."""
    coffee_need = coffee_needs(coffee_type)
    return (
        water >= coffee_need["water"]
        and milk >= coffee_need["milk"]
        and coffee >= coffee_need["coffee"]
    )


def make_coffee(coffee_type):
    global water, milk, coffee, money
    """Makes the specified coffee type and updates resources."""
    coffee_need = coffee_needs(coffee_type)
    if check_resources(coffee_type):
        water -= coffee_need["water"]
        milk -= coffee_need["milk"]
        coffee -= coffee_need["coffee"]
        money += coffee_need["cost"]
        print(f"Dispensing {coffee_type}...")
        time.sleep(2)  # Simulate dispensing time
        print(f"{coffee_type} dispensed!")
    else:
        print("Sorry, not enough resources.")


while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee_type.lower() in ["espresso", "latte", "cappuccino"]:
        print(f"You have selected {coffee_type}.")
        make_coffee(coffee_type)
    elif coffee_type.lower() == "off":
        break
    elif coffee_type.lower() == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")
    else:
        print(
            "Invalid selection. Please try again, you should choose one of these: 'espresso', 'latte', 'cappuccino'."
        )
