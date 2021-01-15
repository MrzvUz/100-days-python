# https://repl.it/@appbrewery/day-2-1-test-your-code#README.md

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆


####################################
# First *fork* your copy. Then copy-paste your code below this line 👇
# Finally click "Run" to execute the tests


# Correct Solution:

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# Check the data type of two_digit_number
print(type(two_digit_number))

# Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

# Add the two digits together.
two_digit_number = first_digit + second_digit

print(two_digit_number)
