number=0
for num in range(1,101):
    number +=num
    if num%3==0 and num%5==0:
        print("fizzbuzz")
    elif num%3==0:
        print("fizz")
    elif num%5==0:
        print("buzz")
    else:
        print(num)

