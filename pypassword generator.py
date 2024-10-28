print("Welcome to PyPassword generator!")
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z' ]
numbers=['0','1','2','3','4','5','6','7','8','9']
symbol=['!','@','#','$','%','&','*','(',')','+']
num_letter=int(input("how many letters would you like in your password?\n"))
num_symbol=int(input("how many symbol would you like ?\n"))
num_number=int(input("how many number would you like?\n"))
#easy level
password=""
for char in range(1,num_letter+1):
    password+=random.choice(letters)
for sym in range(1,num_symbol+1):
    password+=random.choice(symbol)
for num in range(1,num_number+1):
    password+= random.choice(numbers)
print("your password is :",password)
#hard level
password_list=[]
for char in range(1,num_letter+1):
    password_list+=random.choice(letters)
for char in range(1,num_symbol+1):
    password_list+=random.choice(symbol)
for char in range(1,num_number+1):
    password_list+= random.choice(numbers)
random.shuffle(password_list)
password1=""
for char in password_list:
    password1+=char
print("your password is :",password1)
