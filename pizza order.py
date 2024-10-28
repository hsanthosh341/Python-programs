print("welcome to python pizza delivers!")
size=input("enter the size you want ? S,M or L")
add_pepperoni=input("do you want to pepperoni ? Y or N")
extra_cheese=input("do you want extra cheese / Y or N")
prize=0
if size=="S":
    prize+=12
elif size=="M":
    prize+=20
else:
    prize+=25
    
if add_pepperoni=="Y":
    if size=="s":
        prize+=2
    else:
        prize+=3
        
if extra_cheese=="Y":
    prize+=1
print(f"your final bill is ${prize}")
    
