lowercase = [chr(letter) for letter in range(97,123)]
uppercase = [chr(letter) for letter in range(65,91)]

phoneNumber = str(input("Enter a phone number: "))
correct = False
while correct == False:
    verify = str(input(f"Check if what you have entered is correct, press x if not - {phoneNumber}: "))
    if verify == "x":
        phoneNumber = str(input("Enter a phone number: "))
    else:
        correct = True
    
phoneNumberList = list(phoneNumber)
for i in range (len(phoneNumber)):
    for letter in range(0,3):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "2"
    for letter in range(3,6):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "3"
    for letter in range(6,9):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "4"
    for letter in range(9,12):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "5"
    for letter in range(12,15):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "6"
    for letter in range(15,19):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "7"
    for letter in range(19,22):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "8"
    for letter in range(22,25):
        if phoneNumberList[i] == uppercase[letter] or phoneNumberList[i] == lowercase[letter]:
            phoneNumberList[i] = "9"

print ("The valid number corresponding to the number you have entered with letters is: ")
for i in range (len(phoneNumberList)):
    print (phoneNumberList[i],end="")