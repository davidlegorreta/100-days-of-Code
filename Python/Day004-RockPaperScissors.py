# Rock, Paper, Scissors.
import random

random_integer = random.randint(0, 2)

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

print ("_ _ _ _ _ \n \n")

selection_user = int(input ("Please, choose your weapon: \n - Type 0 for Rock \n - Type 1 for Paper \n - Type 2 for Scissors \n \n"))

# User Selection:  

print("\n The user selection was: \n")

if selection_user == 0:
    print(rock)
    print("\n _ _ _ _ _ \n")

elif selection_user == 1:
    print(paper)
    print("\n _ _ _ _ _ \n")

elif selection_user == 2:
    print(scissors)
    print("\n _ _ _ _ _ \n")    

# Computer selection:

print(" The computer selection was: \n \n")

if random_integer == 0:
    print(rock)
    print("\n _ _ _ _ _ \n")

elif random_integer == 1:
    print(paper)
    print("\n _ _ _ _ _ \n")

elif random_integer == 2:Sip
    print(scissors)
    print("\n _ _ _ _ _ \n")  

# Draw Scenario:

if (random_integer == selection_user):
    print ("Drow \n")

# Rock scenario

elif (random_integer == 0) and (selection_user == 1):
    print("You win! \n")
elif (random_integer == 0) and (selection_user == 2):
    print("You lose! \n")

# Paper scenario:

elif (random_integer == 1) and (selection_user == 0):
    print("You lose. \n")
elif (random_integer == 1) and (selection_user == 2):
    print("You win! \n")

# Scissors scenario:

elif (random_integer == 2) and (selection_user == 0):
    print ("You win! \n")
elif (random_integer == 2) and (selection_user == 1):
    print("You lose. \n")

else:
    print("Invalid selection from the user.")