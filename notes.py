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
# names_string = input("Give me everybody\'s names, separated by a comma. ")
# names = names_string.split(", ")
# print(names_string)
# print(names)

# print(len(names))
# random_index = random.randint(0,len(names)-1)
# payer = names[random_index]
# print(f"{payer} is going to buy the meal today!")

# Solution Using random.choice
# payer = random.choice(names)
# print(f"{payer} is going to buy the meal today!")


# Nested Lists

# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# num_of_states = len(states_of_america)
#print(num_of_states)
#print(states_of_america[num_of_states-1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# fruits = ["Strawberries", "Nectarines", "Spinach", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen)

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][2])


# TREASURE MAP EXERCISE
# Write a program that will mark a spot with an X with a two-digit system. The first digit is the vertical column number and the second digit is the horizontal row number


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

# Take the user input and convert to usable format
# Convert first digit to column position
horizontal = int(position[0])
# Convert second digit to row position
vertical= int(position[1]) 

# Update nested list with a "X"
selected_row = map[vertical-1]
selected_row[horizontal -1] = "X"

print(f"{row1}\n{row2}\n{row3}")