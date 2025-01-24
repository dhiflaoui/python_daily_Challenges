
name = input("Enter your name: ")


print(f"Hi, {name}! How are you feeling today?")
print("Please choose a number for your mood:")
print("1. Happy")
print("2. Stressed")
print("3. Tired")


mood_choice = input("Enter the number corresponding to your mood (1, 2, or 3): ")

if mood_choice == "1":
    print(f"That’s great, {name}! Keep spreading your joy!")
elif mood_choice == "2":
    print(f"Take a deep breath, {name}. You're doing amazing!")
elif mood_choice == "3":
    print(f"Rest up, {name}. Tomorrow is a fresh start!")
else:
    print("Invalid choice. Please run the program again and choose 1, 2, or 3.")
