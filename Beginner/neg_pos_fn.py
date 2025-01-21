def pos_neg():
    variable = int(input("Enter a number: "))
    if variable > 0:
        print(f"the Number {variable} is Positive")
    elif variable < 0:
        print(f"the Number {variable} is Negative")
    else:
        print(f"the Number {variable} is a Zero")

pos_neg()