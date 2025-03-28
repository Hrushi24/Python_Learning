print("---------------- Welcome to cointinueos Calculator -----------------")

def add(num1, num2):
    return num1 + num2

def sub(num1 , num2):
    return num1 - num2

def mult(num1 , num2):
    return num1 * num2

def div(num1 , num2):
    try:
        return num1/num2
    except Exception:
        return num1
    

    
calDict = {
    "+" : add ,
    "-" : sub ,
    "*" : mult,
    "/" : div ,
}

calculation  = calDict["*"]

calsiOn = True

num1 = float(input("Enter first number:"))

while(calsiOn == True):
  
    print("Select operator from this below : \n")
    for sign in calDict:
        print(sign + "\n")
    
    selectedOperator = input("Enter operator : ")

    num2 = float(input("Enter 2nd number: "))

    try:
        calculation  = calDict[selectedOperator]
    except Exception:
        print("Selected wrong operetor, default addition done with numbers.")
        calculation = calDict["+"]
    
    total = calculation(num1 , num2)
    # total = calDict[selectedOperator](num1, num2)  
    #  can also use this way.

    print(f"Calculation of {num1} {selectedOperator} {num2} is {total}. ")

    continueChoice = input("Want to continue calculation ? (y/ n) :")
    if(continueChoice == "y"):
        calsiOn = True
        num1 = total
        num2 = 0
    else:
        calsiOn = False

