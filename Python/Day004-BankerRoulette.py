import random

print ("_ _ _ _ _ \n")

# Split string method
names_string = input("Give me everybody's names, separated by a comma: \n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

names_list = names_string.split(", ")

number = int(len(names_list))

value_random = random.randint(1, [number])

lastvalue = (names_list[value_random])

print (f"The person who sill paid the bill wil be {lastvalue}")

print(number)