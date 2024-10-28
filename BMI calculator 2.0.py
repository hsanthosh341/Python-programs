height =float(input("enter your height in m:"))
weight=int(input("enter your weight in kg:"))
value=round(weight/height**2)
if value<18.5:
    print(f"you are UNDERWEIGHT")
elif value<25:
    print(f"your BMI is {value}, you are NORMALWEIGHT")
elif value<30:
    print(f"your BMI is {value}, you are OVERWEIGHT")
elif value<35:
    print(f"your BMI is {value}, you are OBESE")
else:
    print(f"your BMI is {value}, you are CLINICALLY OBESE")
