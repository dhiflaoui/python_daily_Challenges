def main():
    print("Welcome to the Supermarket Billing System!\n")

    # Initialize variables
    items = []  
    tax_rate = 0.05  
    total_discount = 0

    # Input number of items
    try:
        num_items = int(input("Enter the number of items: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Collect item details
    for i in range(num_items):
        print(f"\nItem {i + 1}:")
        name = input("Name: ").strip()
        try:
            price_per_unit = float(input("Price per unit: "))
            quantity = int(input("Quantity: "))
        except ValueError:
            print("Invalid input. Please enter valid numeric values.")
            return

        # Add item to the list
        items.append({"name": name, "price_per_unit": price_per_unit, "quantity": quantity})

    # Display bill summary
    print("\n--- Bill Summary ---")
    subtotal = 0
    for item in items:
        name = item["name"]
        price_per_unit = item["price_per_unit"]
        quantity = item["quantity"]
        item_total = price_per_unit * quantity

        print(f"{name}: {quantity} x ${price_per_unit:.2f} = ${item_total:.2f}")
        subtotal += item_total

    # Calculate discount (if any)
    discounts = {"butter": 0.1, "eggs": 0.05}
    for item in items:
        discount = discounts.get(item["name"].lower(), 0)  
        total_discount += item["price_per_unit"] * item["quantity"] * discount

    # Calculate tax and total
    tax = subtotal * tax_rate
    total = subtotal - total_discount + tax

    # Print summary
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Discount: ${total_discount:.2f}")
    print(f"Sales Tax (5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

    print("\nThank you for shopping with us!")


if __name__ == "__main__":
    main()
