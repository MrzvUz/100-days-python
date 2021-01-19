# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_decimal = random.random() * 5
# print(random_decimal)

# Exercise: https://repl.it/@appbrewery/day-4-1-exercise#README.md
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

# import random

# Heads = input("Heads or Tails?: ")
# randomHeads = random.randint(0, 1)
# user_choice = int(f"{randomHeads}")
# print(user_choice)
# print(randomHeads)

# Correct Solution: https://repl.it/@appbrewery/day-4-1-solution#main.py

import random

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
