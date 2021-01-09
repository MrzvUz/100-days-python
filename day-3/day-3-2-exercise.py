# BMI Calculator: https://repl.it/@appbrewery/day-3-2-exercise#README.md

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
# bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)

print(bmi_as_int)

# Wrong Solution:

if bmi_as_int <= 18.5:
    print("You are underweight.")
    if bmi_as_int > 18.5 and bmi_as_int <= 25:
        print("You have normal weight.")
    elif bmi_as_int > 25 and bmi_as_int <= 30:
        print("You are slightly overweight.")
    elif bmi_as_int > 30 and bmi_as_int <= 35:
        print("You are obese")
else:
    bmi_as_int > 35
    print("You are clinically obese.")

# Correct solution: https://repl.it/@appbrewery/day-3-2-solution#main.py

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
