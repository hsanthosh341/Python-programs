print("***Welcome to tip calculator***")
bill=input("what was the total bill ?  ₹")
tip_percent=input("what  tip would you like to give? 10,12 or 15?")
no_of_person=input("How many people to split the bill?")
tip_percentage=int(bill)*(float(tip_percent)/100)
total_amount=int(bill)+tip_percentage
final_amount=total_amount/int(no_of_person)
amount_for_perperson="{:.2f}".format(final_amount)
print(f"each person should pay : {amount_for_perperson}")
