# Exercise: https://repl.it/@appbrewery/day-4-2-exercise#README.md
# Split string method
# Solution 1:

import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

random_name = random.choice(names)
print(f"{random_name} is going to pay for the meal today.")


# Solution 2: https://repl.it/@appbrewery/day-4-2-solution#main.py

# Split string method
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")

# Write your code below this line 👇

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")
