print('''
*******************************************
T-------------------------------------- I
  R                                               S
     E                                               L
       A                                               A
          S                                               N
            U                                               D
               R                                                             
                  E-------------------------------------
******************************************* ''')
print("Welcome to Treasure Island")
print("Your mission is to find treasure")
get1=input("you're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n ").lower()
if get1=="right":
    print("you fell into a hole. Game over")
if get1=="left":
    get2=input ("You came to lake. There is island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if get2=="swim":
        print("Game over")
    if get2=="wait":
        get3=input("You arrive at the island unharmed. There is a house with 3 doors. One red,one yellow and one blue.Which color do you choose?\n").lower()
        if get3=="red":
            print("It is full of fire.game over")
        elif get3=="blue":
            print("you enter room of beast,game over")
        else:
            print("You found a treasure.lYou win!")
    
