import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
choice=int(input("what do you choose ? Type 0 for rock , 1 for paper or 2 for scissors \n"))
random_choice=random.randint(0,2)
print(f"computer choose:{random_choice}")

if choice==0 and random_choice==2:
    print("you are win")
elif random_choice==0 and choice==2:
    print("you lose")
elif random_choice>choice:
    print("you lose")
elif choice==random_choice:
    print("Draw match")
else:
    print("you enter wrong number,Try again")

