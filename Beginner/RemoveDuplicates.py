
numbers = [3, 1, 2, 3, 4, 1, 5, 2]

unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)


print("List without duplicates:", unique_numbers)
