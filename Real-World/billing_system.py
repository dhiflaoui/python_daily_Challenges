"""
Challenge Title: Supermarket Billing System

Description:
Create a supermarket billing system that allows users to:
1. Input multiple items with their prices and quantities
2. Calculate subtotal, tax, and discounts
3. Generate a detailed bill summary

Examples:
Input: 
- Item 1: Butter, Price: $5.00, Quantity: 2
- Item 2: Eggs, Price: $3.00, Quantity: 1

Output:
--- Bill Summary ---
Butter: 2 x $5.00 = $10.00
Eggs: 1 x $3.00 = $3.00
Subtotal: $13.00
Discount: $1.15 (10% on butter, 5% on eggs)
Tax (5%): $0.65
Total: $12.50

Notes:
- Handles invalid inputs gracefully
- Supports special discounts for specific items
- Includes 5% tax rate on purchases
- Provides clear, formatted output

Tags: real-world, input-handling, calculations, formatting
"""

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

    # Display final calculations
    print(f"\nSubtotal: ${subtotal:.2f}")
    if total_discount > 0:
        print(f"Discount: ${total_discount:.2f}")
    print(f"Tax (5%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()
