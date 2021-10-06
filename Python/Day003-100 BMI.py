#100 days of code: 03 BMI / IMC Calculator. # 
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: \n  \n"))
weight = float(input("enter your weight in kg: \n \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

IMC = str (weight / (height*height))

print ("\n")

print ("Your BMI is: \n" + IMC + "\n")

IMC2 = float(IMC)

if IMC2 < 18.5:
    print ("Underweight \n")
elif IMC2 < 25:
    print ("Normal weight. \n")
elif IMC2 < 30:
    print ("Overweight. \n")
elif IMC2 < 35:
    print ("Obese. \n")
else:
    print ("Clonically obese. \n")

print (" _ _ _ _ _ ")