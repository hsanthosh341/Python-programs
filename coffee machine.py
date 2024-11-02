MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
#available resources in machine
resources = {
    "water":300,
    "milk": 200,
    "coffee": 100,
}
#Function to print available resources
def report():
    print(f"Water :{resources['water']}")
    print(f"Milk :{resources['milk']}")
    print(f"Coffee :{resources['coffee']}")
    print(f"Money:{resources['Money']}")
#Function to check resources sufficient
def resource_sufficient(user_choice):
    if resources['water']>=MENU[user_choice]['ingredients']['water']:
        if resources['coffee']>=MENU[user_choice]['ingredients']['coffee']:
            if user_choice!='espresso':
                if resources['milk']>=MENU[user_choice]['ingredients']['milk']:
                    check_transaction(user_choice)
                else:
                    print("Sorry there is not enough milk")
            else:
                check_transaction(user_choice)
        else:
            print("Sorry there is not enough coffee")
    else:
        print("Sorry there is not enough water")
#declare coins value
Penny=0.01
Nickel=0.05
Dime=0.10
Quarter=0.25
#process coin
def process_coins():
    print("Please insert coins")
    no_of_quarters=int(input("How many quarters?:"))
    value_of_quarters=no_of_quarters*Quarter
    no_of_dimes=int(input("How many dimes?:"))
    value_of_dimes=no_of_dimes*Dime
    no_of_nickles=int(input("How many nickles?:"))
    value_of_nickel=no_of_nickles*Nickel
    no_of_pennies=int(input("How many pennies?:"))
    value_of_pennies=no_of_pennies*Penny
    #return total dollar
    return value_of_dimes+value_of_nickel+value_of_pennies+value_of_quarters
#add element in dictionary
resources['Money']=0
#check transaction
def check_transaction(user_choice):
    user_amount=process_coins()
    if user_amount > MENU[user_choice]['cost']:
        print(f"Here is your ${user_amount - MENU[user_choice]['cost']:.2f}in change.")
        print(f"Here is your {user_choice}☕ Enjoy!")
        manage_resource(user_choice)
        resources['Money']+=MENU[user_choice]['cost']
    elif user_amount == MENU[user_choice]['cost']:
        print(f"Here is your {user_choice}☕ Enjoy!")
        manage_resource(user_choice)
        resources['Money']+= MENU[user_choice]['cost']
    else:
        print("Sorry that's not enough money.Money refunded")
#Function to manage resource
def manage_resource(user_choice):
    resources['water']-=MENU[user_choice]['ingredients']['water']
    resources['coffee']-=MENU[user_choice]['ingredients']['coffee']
    if user_choice!='espresso':
        resources['milk']-=MENU[user_choice]['ingredients']['milk']
continue_process=True
while continue_process:
    user_choice=input("What would you like? (espresso/latte/cappuccino):")
    if user_choice=="report":
        report()
    elif user_choice=="espresso":
        resource_sufficient('espresso')
    elif user_choice=="latte":
        resource_sufficient('latte')
    elif user_choice=="cappuccino":
        resource_sufficient('cappuccino')
    elif user_choice=="off":
        continue_process=False
