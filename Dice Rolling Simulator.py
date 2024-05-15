import random
dice=True
while dice:
 sides=int(input("Enter number of sides:"))
 rolls=int(input("Enter number of rolls:"))
 list=[]
 for i in range (rolls):
  if sides<=0:
    print("Must have atleast one side!!!")
  else:
    face=random.randint(1,sides)
    list.append(face)
 print("\n")
 print("DICE NUMBERS:",list)

 print("\n")
 print("Enter your choice:")
 print("1.Roll again")
 print("2.Quit")
 choice=int(input("enter your choice:"))
 if choice==2:
    dice=False
