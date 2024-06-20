a = 0
b = 0
c = 0
q = '' 

a = int(input("1st num: "))
b = int(input("2nd num: "))
c = int(input("3rd num: "))

#q 
print("Do you want to calculate the product or the sum of these numbers?")
q = input("Type 'product' or 'sum': ").strip().lower() #Забезпечує видалення пробілів + перетворення малих літер 

if q == 'product':
    result = a * b * c
    print(f"The product of the numbers is: {result}")
elif q == 'sum':
    result = a + b + c
    print(f"The sum of the numbers is: {result}")
else:
    print("Invalid input. Please type 'product' or 'sum'.")