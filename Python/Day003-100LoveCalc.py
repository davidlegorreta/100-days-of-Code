# 🚨 Don't change the code below 👇

print("_ _ _ _ _ \n")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

l_name1 = name1.lower()
l_name2 = name2.lower()

# True Counter:

True1 = l_name1.count("t") + l_name1.count("r") + l_name1.count("u") + l_name1.count("e")
True2 = l_name2.count("t") + l_name2.count("r") + l_name2.count("u") + l_name2.count("e")

# Love Counter:

Love1 = l_name1.count("l") + l_name1.count("o") + l_name1.count("v") + l_name1.count("e")
Love2 = l_name2.count("l") + l_name2.count("o") + l_name2.count("v") + l_name2.count("e")

# Print first results:

first_name = int (True1) + int (Love1)
second_name = int (True2) + int (Love2)

print ("_ _ _ _ _ \n")

print (f"The total to the first name is: \n {first_name} \n")
print (f"The total of the second name is:\n {second_name} \n")

print ("_ _ _ _ _ \n")

total_str = str(first_name) + str(second_name)
total = int (total_str)

if (total < 10) or (total > 90):
    print (f"Your score is {total}, you go together like coke and mentos")
elif (total > 40) and (total < 50):
    print (f"Your score is {total}, you are alright together.")
else:
    print (f"Your score is {total}.")

print ("\n _ _ _ _ _ \n")  