#100 Days of Code; Control Flow and Logical Operators#

# If Condition:
# do this
# else:
# do this

# Fist excercise: If Water Level > 80, then drain the water.

water_level = int(input ("Please, add the water level:\n"))
if water_level > 80:
    print("Drain the water.\n")
else:
    print ("Continue.\n")

#_______________________________________________________#

# Odd or Even excercise#
#Modulo operator: %#

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check?\n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print ("This is an Even Number\n")
else:
    print ("This is an Odd Number\n")

# End of the 2nd excercise. 

# 3rd excercise: Nested if / else
#   If contition:
#       if condition:
#           do this
#       else:
#           do this
#   else:
#     do this

print ("Welcme to the rollercoaster! \n")
height = int(input ("What is your height in CM?:\n"))

if height >= 120:
    print("You can ride the Rollercoaster!\n")
    age = int (input ("What's your age?: \n"))
    
    if age <= 18:
        print("Please, pay $7.\n")
    else:
        print("Please, pay $12.\n")
else:
    print("Sorry, you have to grow taller before you can ride. :( \n")
    
    