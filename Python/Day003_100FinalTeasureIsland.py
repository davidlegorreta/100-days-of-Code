print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("\nWelcome to Treasure Island. \n")
print("Your mission is to find the treasure. \n") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

side01 = input ("You're at a cross road. Where do youu want to go? \n -Left or Right? \n \n  ")
side = side01.lower()

if side == "left":
    swim01 = input ("\n Congrats! You can continue. \n \n There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n \n Select, swim or wait: \n  ")
    swim = swim01.lower()

    if swim == "wait":
        door01 = input("\n You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n - Red, yellow or blue? \n  ")
        door = door01.lower()

        if door == "red":
            print("\n It's a room full of fire. Game Over.\n") 

        elif door == "yellow":
            print("\n You found the treasure! You Win!\n")
            
        else:
            print("\n You chose a door that doesn't exist. Game Over.\n")
    else:
        print("\n You get attacked by an angry sharknado. Game Over.\n")
else:
    print("\n You fell into a hole. Game Over.\n")
