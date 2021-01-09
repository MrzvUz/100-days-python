# Checking the year whether it is a leap your or not: https://repl.it/@appbrewery/day-3-3-exercise#README.md

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if year % 4 == 0:
    print(f"The year {year} is a leap year")
else:  # year % 4 != 0:
    print(f"This {year} is not a leap year.")


# Correct Solution: https://repl.it/@appbrewery/day-3-3-solution#main.py

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Refer to the flow chart here: https://bit.ly/36BjS2D

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
