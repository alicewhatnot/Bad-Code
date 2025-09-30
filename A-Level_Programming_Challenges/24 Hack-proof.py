import random

def createUser(password):
    '''Creating a username and password'''
    while True:
        username = str(input("Enter a username: "))
        usingDefault = str(input(f"Use the default suggested password: {password} (y/n): "))
        if usingDefault == "n":
            #Checking if the password has enough length/detail
            while True:
                detail = False
                length = False
                password = str(input("Enter a password: "))
                specialCharacters = [chr(letter) for letter in range(33,48)]+[chr(letter) for letter in range(58,65)]+[chr(letter) for letter in range(91,97)]+[chr(letter) for letter in range(124,127)]
                if any(c in specialCharacters for c in password):
                    detail = True
                if len(password)>8:
                    length = True
                if detail == True and length == True:
                    break
                print ("Sorry, your password is not strong enough.")
            check = str(input("Check password? (y/n): "))
            if check == "y":
                print (f"Password entered: {password}")
        print (f"Username entered: {username}")
        check = str(input("Are these details correct? (y/n): "))
        if check == "y":
            break
    return username,password

def randomPassword():
    '''Creating a random password to suggest'''
    characters = [chr(letter) for letter in range(33,123)]
    password = ""
    for i in range(8):
        password = password+random.choice(characters)
    return password
    
def openFile(username,password):
    '''Opening file if details are correct'''
    detailsCorrect = False
    for i in range (3):
        if i >= 1:
            print ("Sorry, that wasn't correct.")
        usernameEntered = str(input("Enter a username: "))
        passwordEntered = str(input("Enter a password: "))
        if usernameEntered == username and passwordEntered == password:
            detailsCorrect = True
            break
        if i == 2:
            print ("Sorry, you have no more guesses.")
    if detailsCorrect == True:
        print ("The contents of the file are: ")
        text_file = open("SecretFile.txt","r")
        for line in text_file:
            print (line)
        text_file.close()


# Main Program
username = ""
password = randomPassword()
username,password = createUser(password)
print ("\n")
wantFile = str(input("Show the contents of the file? (y/n): "))
if wantFile == "y":
    openFile(username,password)

        
        
        
    