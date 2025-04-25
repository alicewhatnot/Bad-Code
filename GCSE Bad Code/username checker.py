roomNumValid = "false"
roomNumber = ""
while roomNumValid == "false":
    roomNumber = str(input("Enter a room number"))
    while len(roomNumber) != 3:
        roomNumber = str(input("not a valid room number"))
    roomLetter = roomNumber[0]
    roomDigits = roomNumber[1]+roomNumber[2]
    if roomLetter.isalpha():
        if roomLetter.isupper():
            if roomDigits.isdigit():
                roomNumValid = "true"
                print ("true")
    else:
        print ("not a valid room number")
        