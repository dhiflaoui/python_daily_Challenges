grocery_list = {
    "apples": 5,
    "bananas": 2,
    "milk": 1,
    "bread": 1
}
# Multiply the quantity of each item by 10
for item, quantity in grocery_list.items():
    grocery_list[item] = quantity * 10

print(f"Updated Grocery List: {grocery_list}")
