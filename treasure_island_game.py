#This is a treasure island game where you find a treasure


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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("Welcome to the Treasure Island! \nYour mission is to find the treasure.")
choice1 = input("You're at the crossroad, where do you want to go? Type 'left' or 'right'.").lower()


if choice1 == "left":
  choice2 = input("You have came to a lake. There is an island in middle of lake. Type 'wait' if you want to wait for boat or 'swim' if you want to swim. ").lower()
  if choice2 == "wait":
    choice3 = input("You have reached the island unharmed.this is a house with 3 doors. One is red, one yellow and one blue. Which one do you choose?").lower()
    if choice3 == "red":
      print("Uh-Oh! You are burned by the fire. GAME OVER")
    elif choice3 == "yellow":
      print("Congratulations, You have found the treasure. You Win!")  
    elif choice3 == "blue":
      print("Uh-oh! You are eaten by the beasts. GAME OVER")
    else:
      print("GAME OVER")
  else:
    print("Oh-no...You've got attacked by trouts. GAME OVER")
else:
  print("Oops...You fall into a hole. GAME OVER")


