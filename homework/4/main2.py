a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))


print("What do you want to calculate?")
print("Type 'maximum' to find the maximum of the numbers")
print("Type 'minimum' to find the minimum of the numbers")
print("Type 'average' to find the average of the numbers")

#choice
choice = input("Enter your choice: ").strip().lower()

#calculation
if choice == 'maximum':
    result = max(a, b, c)
    print(f"The maximum of the numbers is: {result}")
elif choice == 'minimum':
    result = min(a, b, c)
    print(f"The minimum of the numbers is: {result}")
elif choice == 'average':
    result = (a + b + c) / 3
    print(f"The average of the numbers is: {result:.2f}")
else:
    print("Invalid input. Please type 'maximum', 'minimum', or 'average'.")
