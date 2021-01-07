# 1. Create a greeting for your program.

# 2. Ask the user for the city that they grew up in.

# 3. Ask the user for the name of a pet.

# 4. Combine the name of their city and pet and show them their band name.

# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

# Solution:

# 1. Create a greeting for your program.
print("Welcome to the Band Name Generator!")

# 2. Ask the user for the city that they grew up in.
city_name = input("In what city did you grew up?: ")

# 3. Ask the user for the name of a pet.
pet_name = input("What is the name of your pet?: ")

# 4. Combine the name of their city and pet and show them their band name.
print("So your band's name should be: " + city_name + " " + pet_name)

# 5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/

# Correct solution:
print("Welcome to the Band Name Generator.")
street = input("What's name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)

# Cleaner way to get the output using f string formatting.
print(f"Your band name could be {street} {pet}")



