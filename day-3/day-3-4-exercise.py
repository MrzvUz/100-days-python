# Python Pizza Delivery app exercise: https://repl.it/@appbrewery/day-3-4-exercise#README.md

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?: ")
add_pepperoni = input("Do you want pepperoni? Y or N?: ")
extra_cheese = input("Do you want extra cheese? Y or N?: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

S = 15
M = 20
L = 25
Y = 0

add_pepperoni = Y
extra_cheese = Y

if size == S:
    S = 15
    if add_pepperoni == Y:
        S += 2
    if extra_cheese == Y:
        S += 1
    print(f"Your total bill is ${S}")
else:
    print("You can not order.")


# Correct Solution: https://repl.it/@appbrewery/day-3-4-solution#main.py

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L?: ")
add_pepperoni = input("Do you want pepperoni? Y or N?: ")
extra_cheese = input("Do you want extra cheese? Y or N?: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
