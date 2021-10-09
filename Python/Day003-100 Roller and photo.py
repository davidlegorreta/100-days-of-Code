print (" _ _ _ _ _ \n")

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# This variable (bill) sets the inicial value of this variable. SO, after the conditionals, the value will change for the updated value.

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")

  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")
  print (" _ _ _ _ _ \n")

else:
  print("Sorry, you have to grow taller before you can ride.")
  print (" _ _ _ _ _ \n")