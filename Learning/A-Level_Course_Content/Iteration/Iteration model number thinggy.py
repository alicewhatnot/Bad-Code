oldModels = 0
total = 0
partNumber = 0
while partNumber != "9999":
    partNumber = input("Enter a part number: ")
    while (len(partNumber) != 4):
        partNumber = input("Invalid part number, please try again: ")
    if (partNumber[3:]) == "6" or partNumber[3:] == "7" or partNumber[3:] == "8":
        oldModels = oldModels + 1
    total = total + 1
print ("There were",oldModels,"old models.")
print ("There were",total-1,"total parts")