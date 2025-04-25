print ("1:Economy Car")
print ("2:Saloon Car")
print ("3:Sports Car")
carChoice = int(input("Enter car choice: "))
if carChoice == 1:
    proceeding = input("Proceed? (y/n)")
    if proceeding == "y":
        print ("You chose: Economy Car")
elif carChoice == 2:
    proceeding = input("Proceed? (y/n)")
    if proceeding == "y":
        print ("You chose: Saloon Car")
elif carChoice == 3:
    proceeding = input("Proceed? (y/n)")
    if proceeding == "y":
        print ("You chose: Sports Car")

