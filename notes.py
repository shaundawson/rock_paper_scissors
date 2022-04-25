# Randomisation and Python Lists
import random

# create random whole number
# random_integer = random.randint(1, 10)
# print(random_integer)

# create random floating point - between [0.0 to 1.0)
# random_float = random.random()

# love_score = random.randint(1,100)
# print(f"Your love score is: {love_score}")

# HEADS OR TAILS EXERCISE
# Write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")
