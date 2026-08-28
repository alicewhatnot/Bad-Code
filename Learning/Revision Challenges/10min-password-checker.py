def charType(character):
    ordinal = ord(character)
    if ordinal >= 65 and ordinal <= 90:
        return "Upper"
    elif ordinal >= 97 and ordinal <= 122:
        return "Lower"
    elif (ordinal >= 33 and ordinal <= 47) or (ordinal >= 58 and ordinal <= 64) or (ordinal >= 91 and ordinal <= 96) or (ordinal >= 123 and ordinal <= 126):
        return "Special"
    elif (ordinal >= 48 and ordinal <= 57):
        return "Number"

valid = False
while not valid:
    password = str(input("Enter a password: "))

    upper = False
    lower = False
    number = False
    special = False
    length = False

    for char in password:
        if charType(char) == "Upper":
            upper = True
        elif charType(char) == "Lower":
            lower = True
        elif charType(char) == "Number":
            number = True
        elif charType(char) == "Special":
            special = True
    
    length = len(password) > 10
        
    if upper and lower and number and special and length:
        valid = True
    else:
        upper = False
        lower = False
        number = False
        special = False
        length = False

print ("Password Accepted")


    