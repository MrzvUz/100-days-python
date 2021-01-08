# https://repl.it/@appbrewery/day-2-2-exercise#README.md

# Wrong Solution:

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests
print(type(height))
print(type(weight))

body_size = int(weight) / float(height) ** 2
result = float(body_size) * float(height)

print(result)


# Solution:
# https://repl.it/@appbrewery/day-2-2-solution#main.py

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)
