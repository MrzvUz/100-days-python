# import random

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random()
# print(random_float)

# random_decimal = random.random() * 5
# print(random_decimal)

# Exercise:
# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

import random

Heads = input("Heads or Tails?: ")
randomHeads = random.randint(0, 1)
user_choice = int(f"{randomHeads}")
print(user_choice)
print(randomHeads)
