import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper,scissors]

#Store the user's input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >=3 or user_choice < 0:
  print("You typed an invlaid number, you lose.")
else:
    print("User chose:")
    print(game_images[user_choice])
  
    #Store the computer's input
    computer_choice = random.randint(0,2)
    print("Computer chose:")
    print(game_images[computer_choice])
    
    # if user choice is rock and computer choice is scissors, you win
    if user_choice == 0 and computer_choice == 2:
      print("You win!")
    # if computer choice is rock and user choice is scissors, you lose
    elif computer_choice == 0 and user_choice == 2:
      print("You lose")
      # if computer choice is paper and user choice is rock or if computer choice is scissors and user choice is paper, you lose
    elif computer_choice > user_choice:
      print("You lose.")
      # if user choice is paper and computer choice is rock or if user choice is scissors and computer choice is paper, you win
    elif user_choice > computer_choice:
      print("You win!")
      # if choices are equal it's a draw
    elif computer_choice == user_choice:
      print("It\'s a draw.")