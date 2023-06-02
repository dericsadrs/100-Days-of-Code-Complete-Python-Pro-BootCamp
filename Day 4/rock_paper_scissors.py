#
# Created on Fri Jun 02 2023
# Created by Software Engineer Deric San Andres
#
import random

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

choices = [rock, paper, scissors]
choice = int(input("What do you choose? Ty)pe 0 for Rock, 1 for Paper, 2 for Scissprs: "))

if choice == 0 or choice == 1 or choice == 2:
   print(choices[choice],"\n")
   computer_choice = random.randint(0,2)
   print(f"Computer chose: {choices[computer_choice]}")
    
   if choice == 0 and computer_choice == 2:
        print("You win!")
   elif computer_choice == 0 and choice == 2:
       print("You lose!")
   elif computer_choice > choice:
        print("You lose!")
   elif choice > computer_choice:
       print("You win!")
   elif computer_choice == choice:
       print("It's a draw")
   else:
       print("You typed an invalid nubmer, you lose!")