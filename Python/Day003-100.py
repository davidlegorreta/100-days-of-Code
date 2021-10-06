#100 Days of Code; Control Flow and Logical Operators#

# If Condition:
# do this
# else:
# do this

# Fist excercise: If Water Level > 80, then drain the water.

print (" _ _ _ _ _ \n")

water_level = int(input ("Please, add the water level:\n"))
if water_level > 80:
    print("Drain the water.\n")
else:
    print ("Continue.\n")

print (" _ _ _ _ _ \n")

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

print (" _ _ _ _ _ \n")
# End of the 2nd excercise. 

# ________________ #

"""
# 3rd excercise: Nested if / else
#   If contition:
#       if condition:
#           do this
#       else:
#           do this
#   else:
#     do this

"""

print ("Welcome to the rollercoaster! \n")
height = int(input ("What is your height in CM?:\n"))

if height >= 120:
    print("You can ride the Rollercoaster!\n")
    age = int (input ("What's your age?: \n"))
    
    if age <= 18:
        print ("Please, pay $7.\n")
    else:
        print ("Please, pay $12.\n")
else:
    print ("Sorry, you have to grow taller before you can ride. :( \n")

""" 
IF / ELIF / ELSE

if condition1:
    do A
elif condition2
    do B
else:
    do this.

"""

print (" _ _ _ _ _ \n")

# Same case, but now with "elif. #
# "
print ("Welcome to the rollercoaster! \n")
height2 = int(input ("What is your height in CM?:\n"))


if height2 >= 120:
    print ("You can ride the Rollercoaster!\n")
    age2 = int (input ("What's your age?:\n"))

    if age2 < 12:
        print ("Please, pay $5. \n")

    elif age2 <= 18:
        print ("Please, pay $7. \n") 
    
    else:
        print ("Please, pay $12- \n")

else:
    print ("Sorry, you have to grow taller before you can ride. :( \n") 

print (" _ _ _ _ _ ")