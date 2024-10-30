import random
print('''   
 ___  ___  ___  ________  ___  ___  _______   ________         
|\  \|\  \|\  \|\   ____\|\  \|\  \|\  ___ \ |\   __  \        
\ \  \\\  \ \  \ \  \___|\ \  \\\  \ \   __/|\ \  \|\  \       
 \ \   __  \ \  \ \  \  __\ \   __  \ \  \_|/_\ \   _  _\      
  \ \  \ \  \ \  \ \  \|\  \ \  \ \  \ \  \_|\ \ \  \\  \|     
   \ \__\ \__\ \__\ \_______\ \__\ \__\ \_______\ \__\\ _\     
    \|__|\|__|\|__|\|_______|\|__|\|__|\|_______|\|__|\|__|    
                                                               
                                                                                                                             
 ___       ________  ___       __   _______   ________         
|\  \     |\   __  \|\  \     |\  \|\  ___ \ |\   __  \        
\ \  \    \ \  \|\  \ \  \    \ \  \ \   __/|\ \  \|\  \       
 \ \  \    \ \  \\\  \ \  \  __\ \  \ \  \_|/_\ \   _  _\      
  \ \  \____\ \  \\\  \ \  \|\__\_\  \ \  \_|\ \ \  \\  \|     
   \ \_______\ \_______\ \____________\ \_______\ \__\\ _\     
    \|_______|\|_______|\|____________|\|_______|\|__|\|__|    
                                                                                                                                                                                        
''')
VS='''          
__   _____ 
\ \ / / __|
 \ V /\__ /
  \_/ |___/            
'''
current_score=0
name_list1=['Cristiano Ronaldo','Instagram Official Account','Selena Gomez',
                 'National Geographic','Dwayne "The Rock" Johnson','Billie Eilish','Zendaya',
                 'Justin Bieber','FC Barcelona','Shakira']
name_list2=['Kylie Jenner','Lionel Messi','Kim Kardashian','Nike','Taylor Swift',
       'Ariana Grande','Beyoncé','Kendall Jenner','Real Madrid','Miley Cyrus']
correct_option=['Cristiano Ronaldo','Instagram Official Account','Selena Gomez','Nike','Dwayne "The Rock" Johnson',
        'Ariana Grande','Beyoncé','Justin Bieber','Real Madrid','Shakira']
def question():
    print(f"Compare A :{name_list1[random_number]}")
    print(VS)
    print(f"Against B :{name_list2[random_number]}")
def check_answer():
    if correct_option[random_number] == name_list1[random_number]:
        return name_list1[random_number]
    elif correct_option[random_number]==name_list2[random_number]:
        return name_list2[random_number]
def get_input():
    choice=input("Who has more followers?Type 'A' or 'B':")
    if choice=='a':
        return name_list1[random_number]
    elif choice=='b':
        return name_list2[random_number]
continue_game=True
while continue_game:
    random_number = random.randint(0, 9)
    question()
    answer=check_answer()
    user_choice=get_input()
    if answer==user_choice:
        current_score+=1
        print(f"You are rigth!,Your current score: {current_score}")
    else:
        print(f"Sorry,that's wrong. Final score:{current_score}")
        continue_game=False






