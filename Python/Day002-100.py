# Tips calculator.input
# Welcome line:
print ("Welcome to the tip calculator: \n")
#Ask for the first total. 
total_paid = input ("What's the total of the bill?: \n")
#Ask for the people to split the total:
people_split = input ("How many people to split?: \n")
#Ask for the percentage tip.
tip_percentage = input ("What percentage would you like to give? 10, 12 or 15?: \n")

#FInal line:

new_total_paid = float(total_paid)
new_people_split = float(people_split)
new_tip_percentage = float(tip_percentage)

total_1 = new_total_paid / 100
total_2 = total_1 * new_tip_percentage
total_3 = (total_2 + new_total_paid) / new_people_split

total_str = str(total_3)


print ("Each person shoud pay: $ " + total_str)