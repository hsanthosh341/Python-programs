age = input("enter your age :")
days=90*365
weeks=90*52
month=90*12
age1=int(age)
x=days-age1*365
y=weeks-age1*52
z=month-age1*12
print(f"You have {x} days, {y} weeks,and {z} months left.")
