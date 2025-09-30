def menu():
    print ("Enter 1 to encode a string.\n"
           "Enter 2 to print the encoded string.\n"
           "Enter 3 to unencode a string.\n"
           "Enter 4 to quit.")
    try:
        choice = str(input())
        if choice == "1" or choice == "2" or choice == "3":
            return choice
        else:
            raise Exception
            return False
    except:
        print ("Sorry, invalid choice.\n")
        
def getInteger(text):
    while True:
        try:
            if text == "a":
                userInput = int(input("Enter the amount of places to move a letter. \n"))
            else:
                userInput = int(input("Enter the amount of places the letters have been moved. \n"))              
            return userInput
        except:
            print("Invalid entry. Try again.\n")
            
def encodeString():
    moveAmount = getInteger("a")
    string = str(input("Enter a string. \n"))
    stringEncoded = []
    for i in range (len(string)):
        encoded = ord(string[i])+moveAmount
        while encoded > 127:
            encoded = encoded - 127
        stringEncoded.append(encoded)
    return stringEncoded

def printEncoded(stringEncoded):
    print ("The encoded string is: ",end="")
    for i in range (len(stringEncoded)):
        print (chr(stringEncoded[i]),end="")
    print ("\n")

def decodeString():
    moveAmount = getInteger("b")
    string = str(input("Enter the string. \n"))
    decodedArray = []
    for i in range (len(string)):
        decoded = ord(string[i])-moveAmount
        while decoded < 33:
            decoded = decoded + 127
        decodedArray.append(decoded)
    print ("The decoded string is: ",end="")
    for i in range (len(decodedArray)):
        print (chr(decodedArray[i]),end="")
        if decodedArray[i] == 159:
            print (" ",end="")
    print ("\n")
    print (decodedArray)

while True:
    choice = menu()
    if choice == "1":
        stringEncoded = encodeString()
    if choice == "2":
        try:
            printEncoded(stringEncoded)
        except:
            print ("Sorry, you need to encode a string first.\n")
    if choice == "3":
        decodeString()
    if choice == "4":
        break
    
    