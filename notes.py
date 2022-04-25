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

# random_side = random.randint(0, 1)
# if random_side == 1:
#     print("Heads")
# else:
#     print("Tails")


# Lists - Understanding the Offset and Appending Items to Lists

# List of states by date of admission to the Union
# states_of_america = ["Delaware", "Pensylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# Get first state in list
# print(states_of_america[0])

# Get last state in the list
# print(states_of_america[-1])

# Correct State Name 
# states_of_america[1] = "Shondaland"
# print(states_of_america)

# Add State to the end of list
# states_of_america.append("Mexico")
# print(states_of_america)

# Add a whole bunch of items to the list
# states_of_america.extend(["Shaunland", "Nandiland", "Tracyland", "Milaunland", "Kalenaland", "Courtneyland" "Royland", "Johnnyland"])
# print(states_of_america)


# BANKER ROULETTE EXERCISE
# Split string method
names_string = input("Give me everybody\'s names, separated by a comma. ")
names = names_string.split(", ")
# print(names_string)
# print(names)

# print(len(names))
random_index = random.randint(0,len(names)-1)
payer = names[random_index]
print(f"{payer} is going to buy the meal today!")
