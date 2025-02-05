"""
Project Description
In this project, you’ll create a simple program that organizes a shopping list.

You can start by placing this list in the first line of your Python script:

shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]
Your program should do the following:

*Sort the items of the list alphabetically

*Remove duplicates


"""

shopping_list = ["apples", "bananas", "oranges", "milk", "bananas", "bread", "apples"]
unique_sorted_list = sorted(set(shopping_list))
print("Organized Shopping List:")
for item in unique_sorted_list:
    print(item)



