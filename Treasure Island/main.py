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
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

path1 = input("There are 2 ways in the fog. Which way do you prefer left or right?\n").lower()
if path1 == "left":
    path2 = input("You arrive the death lake. Are you gonna wait or swim\n?").lower()
    if path2 == "wait":
        path3 = input("You are arrived the castle. There are 3 doors which one do you prefer red, yellow or blue?\n").lower()
        if path3 == "red":
            print("You are dead. You've got burn.")
        elif path3 == "blue":
            print("You are dead. You are fall into a pit.")
        elif path3 == "yellow":
            print("You won. You found a trasure!")
        else:
            print("You are dead. You've shocked by a ghost.")
    else:
        print("You are dead. You've been eaten by a sea monster.")
else:
    print("You are dead. You've lost track and attacked by a wild animal.")
    
