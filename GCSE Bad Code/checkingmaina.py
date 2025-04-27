usernameValid = "false"
username = ""
while usernameValid == "false":
    username = str(input("Enter a username: "))
    if username.isalpha():
        usernameValid = "true"
    else:
        print ("Username invalid")
        
idValid = "false"
id = ""
while idValid == "false":
    id = str(input("Enter a valid id: "))
    idStart = id[1]+id[2] 
    if idStart == "ID":
        idValid = "true"
    else:
        print ("ID invalid")

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
        