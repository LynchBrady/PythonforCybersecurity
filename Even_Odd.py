#Asks the user for a number
number = int(input("Enter your number here: "))

#Divides the input by 2 to see if it's odd
if number % 2 == 0:
    print(f"{number} is an even number!")
else:
    print(f"{number} is an odd number!" )    