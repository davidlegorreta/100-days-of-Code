import random

print ("_ _ _ _ _ \n")

# Split string method
names_string = input("Give me everybody's names, separated by a comma: \n ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

num_items = len(names)

random_choice = random.randint(0, num_items - 1)

person_who_will_pay = names [random_choice]

print (person_who_will_pay + " is going to buy the meal today. \n")

person_who_will_pay_2 = random.choice(names)

print (person_who_will_pay_2 + " is going to buy the meal today. \n")

print ("_ _ _ _ _ \n")