VAT = 0.2
choice = ""
anotherCalculation = "True"
while anotherCalculation == "True":
    print ("Enter v for VAT, t for tax and k for kilos to pounds")
    choice = str(input("Choose which calculator you want to use: "))
    if choice == "v":
        number = float(input("Enter the value to have VAT calculated on: "))
        vatCalculation = (number+number*VAT)
        print ("The VAT on",number,"brings the total to:",vatCalculation)
    elif choice == "t":
        number = float(input("Enter the value to have tax calculated on: "))
        taxRate = float(input("Enter the percentage tax rate: "))
        numberTaxed = number*(taxRate/100)
        print ("The tax on",number,"brings the total to:",numberTaxed)
    elif choice == "k":
        number = float(input("Enter an amount in kilos: "))
        numberPounds = number*2.205
        print (number,"kilos is",numberPounds,"in pounds")
    else:
        print ("Invalid input")
    continuing = str(input("Enter another calculation?: (y/n) "))
    if continuing == "y":
        anotherCalculation = "True"
    else:
        anotherCalculation = "False"


