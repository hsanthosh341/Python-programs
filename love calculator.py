print("WELCOME TO THE LOVE CALCULATOR")
name1=input("what is your name?\n")
name2=input("what is their name?\n")
lower_name1=name1.lower()
lower_name2=name2.lower()
names=lower_name1+lower_name2
print(names)
t=names.count("t")
r=names.count("r")
u=names.count("u")
e=names.count("e")
l=names.count("l")
o=names.count("o")
v=names.count("v")
e=names.count("e")
true=str(t+r+u+e)
love=str(l+o+v+e)
score=int(true+love)
if score<10 or score>90:
    print(f"your score is {score}, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print(f"your score is {score},you are alright together.")
else:
    print(f"your score is {score}")

