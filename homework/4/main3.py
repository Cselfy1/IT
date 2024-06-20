METERS_TO_MILES = 0.000621371
METERS_TO_INCHES = 39.3701
METERS_TO_YARDS = 1.09361

meters = float(input("Enter the distance in meters: "))

#q
print("What do you want to convert the meters to?")
print("Type 'miles' to convert to miles")
print("Type 'inches' to convert to inches")
print("Type 'yards' to convert to yards")

#choice
choice = input("Enter your choice: ").strip().lower()

if choice == 'miles':
    result = meters * METERS_TO_MILES
    print(f"{meters} meters is equal to {result:.6f} miles")
elif choice == 'inches':
    result = meters * METERS_TO_INCHES
    print(f"{meters} meters is equal to {result:.2f} inches")
elif choice == 'yards':
    result = meters * METERS_TO_YARDS
    print(f"{meters} meters is equal to {result:.2f} yards")
else:
    print("Invalid input. Please type 'miles', 'inches', or 'yards'.")