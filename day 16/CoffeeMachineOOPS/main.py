from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



CofMacker = CoffeeMaker()
menu = Menu()
moneyMach = MoneyMachine()

state = True

print("Welcome to coffee maker , Enjoy Coffee with us.")


while(state):
    userInput = input("What would you like ? (latte, espresso, cappuccino)? or turn 'off'? ")

    if(userInput == "report"):
        CofMacker.report()
        moneyMach.report()
    elif(userInput == "off"):
        state = False

    elif(userInput == "latte" or userInput == "espresso" or userInput == "cappuccino"):
        canMake = CofMacker.is_resource_sufficient(menu.find_drink(userInput))

        if(canMake == True):
            itemNeeded = menu.find_drink(userInput)
            paymentStatus = moneyMach.make_payment(itemNeeded.cost)

            if(paymentStatus == True):
                CofMacker.make_coffee(menu.find_drink(userInput))
                choice = input("Would you like to order more? (y/n) :")
                if(choice  == "y"):
                    state = True
                else:
                    state = False
            else:
                print("Money not sufficent, money returned and order canceled.")
        else:
            print(f"Sorry not sufficent resources for {userInput}")
    else:
        print("Please enter correct order.")
