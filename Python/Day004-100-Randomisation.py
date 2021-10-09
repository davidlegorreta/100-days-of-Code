#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲

import random

random_integer = random.randint(1, 2)

if random_integer == 1:
    print ("\n Heads. \n")

else:
    print ("\n Tails. \n")

print ("\n _ _ _ _ _ \n")

#  How to store pieces of information #
# a = 3.
# b = hello
# To grupo the people in one variable, we can use list:
# fruits = [item1, item2] 
# fruits = ["Cherry", "Apple", "Pear"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

states_of_america[1] = "Pencilbania"

print(states_of_america)

states_of_america.append ("Puerto Rico Juas Juas")

print(states_of_america)

states_of_america.extend(["Mapacheland", "Durango", "Guam"])

print(states_of_america)

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

