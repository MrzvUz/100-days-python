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
