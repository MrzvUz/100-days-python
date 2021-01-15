# # Control Flow with if/else and Conditional Operators

# print("Welcome to the rollercoaster!")
# height = int(input("What is your height ub cm?"))

# if height >= 120:
#     print("You can ride the rollercoaster!")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# Odd or Even? Exercise: https://repl.it/@appbrewery/day-3-1-exercise#README.md

pick_num = int(input("Which number do you want to check?: "))

if pick_num % 2 == 0:
    print("Your number is even.")
else:
    print("Your number is odd number")


# Solution: https://repl.it/@appbrewery/day-3-1-solution#main.py

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

# If the number can be divided by 2 with 0 remainder.
if number % 2 == 0:
    print("This is an even number.")
# Otherwise (number cannot be divided by 2 with 0 remainder).
else:
    print("This is an odd number.")


# Conditional statement nested inside with another conditional statement: https://repl.it/@appbrewery/day-3-end#main.py

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")
