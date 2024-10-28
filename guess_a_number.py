import random
print('''
   _____ _    _ ______  _____ _____              _   _ _    _ __  __ ____  ______ _____  
  / ____| |  | |  ____|/ ____/ ____|     /\     | \ | | |  | |  \/  |  _ \|  ____|  __ \ 
 | |  __| |  | | |__  | (___| (___      /  \    |  \| | |  | | \  / | |_) | |__  | |__) |
 | | |_ | |  | |  __|  \___ \\___ \    / /\ \   | . ` | |  | | |\/| |  _ <|  __| |  _  / 
 | |__| | |__| | |____ ____) |___) |  / ____ \  | |\  | |__| | |  | | |_) | |____| | \ \ 
  \_____|\____/|______|_____/_____/  /_/    \_\ |_| \_|\____/|_|  |_|____/|______|_|  \_\   
                                                                                                                                                                                
''')
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level=input("Choose a difficulty. Type 'easy' or 'hard':")
attempt=0
#To check game difficulty
if level=="easy":
    attempt=10
else:
   attempt=5
answer=random.randint(0,100)
#To check the answer for game
for i in range(attempt):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess=int(input("Make a guess:"))
    if guess==answer:
        print("you are WIN!")
        break
    elif guess>answer:
        print("Too high.")
        attempt-=1
    elif guess<answer:
        print("Too low.")
        attempt-=1
    if attempt==0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")

      


