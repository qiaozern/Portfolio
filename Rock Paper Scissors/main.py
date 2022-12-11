"""
0 = Rock
1 = Paper
2 = Scissors
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice_list = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
com_choice = random.randint(0, 2)

print(f"{choice_list[choice]}\nComputer chose:\n{choice_list[com_choice]}")


if choice >= 3 or choice <= 0:
    print("Invalid input, you lose!")
elif choice == com_choice:
    print("Draw!")
elif choice == 0 and com_choice == 2:
    print("You Win!")
elif choice == 2 and com_choice == 0:
    print("You lose!")
elif choice > com_choice:
    print("You Win!")
else:
    print("You lose!")