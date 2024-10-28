print("WELCOMR TO ROLLERCOASTER")
height=int(input("what is your height in cm ?"))
bill=0
if height>120:
    print("You can ride in rollercoaster")
    age=int(input("What is your age ?"))
    if age<12:
        bill=5
        print("child ticket are $5.")
    elif age<=18:
        bill=7
        print("youth ticket are $7.")
    elif age>=45 and age<=55:
        bill=0
        print("everything is going to be ok, Have a free ride on us!")
    else:
        bill=12
        print("adult ticket are $12.")
    want_photo=input("do you want a photo taken? yes or no ")
    if want_photo=="yes":
        bill+=3
    print(f"your final bill is ${bill}")
else:
    print("You have to grow taller before you  can ride. ")
    
