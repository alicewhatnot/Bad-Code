def getString(firstString):
    while True:
        try:
            userInput = str(input("Enter another string: "))
            if len(userInput) != len(firstString):
                raise Exception
            return userInput
        except:
            print("Sorry! The strings have to be the same length!")
            
def stringToASCII(string):
    stringArray = []
    for i in range (len(string)):
        asciiVal = (ord(string[i]))
        stringArray.append(asciiVal)
    return stringArray

def subtractingStrings(firstStringASCII,secondStringASCII):
    subtractedASCII = []
    for i in range (len(firstStringASCII)):
        subtractedASCII.append(firstStringASCII[i]-secondStringASCII[i])
    return subtractedASCII

def printFinalASCII(subtractedASCII):
    for i in range (len(subtractedASCII)):
        print (subtractedASCII[i],end=" ")
    print ("")    

def menu():
    print ("Enter 1 to subtract the second string from the first","\n"
           "Enter 2 to remove the characters in the second string that are present in the first","\n"
           "Enter 3 to perform both actions")
    while True:
        try:
            userInput = str(input())
            if userInput == "1" or userInput == "2" or userInput == "3":
                return userInput
            else:
                raise Exception
        except:
            print("Sorry! That was an invalid input!")

def removingRepetition(firstStringASCII,secondStringASCII):
    for i in range (len(firstStringASCII) - 1, -1, -1):
        if firstStringASCII[i] == secondStringASCII[i]:
            secondStringASCII.pop(i)

def printString(string):
    for i in range (len(string)):
        print (chr(string[i]),end="")
    print ("")
    
firstString = input("Enter a string: ")
secondString = getString(firstString)
firstStringASCII = stringToASCII(firstString)
secondStringASCII = stringToASCII(secondString)
userInput = menu()
if userInput == "1" or userInput == "3":
    subtractedASCII = subtractingStrings(firstStringASCII,secondStringASCII)
    print ("The final number values for the subtracted strings is:")
    printFinalASCII(subtractedASCII)
    print ("")
if userInput == "2" or userInput == "3":
    removingRepetition(firstStringASCII,secondStringASCII)
    print ("After removing repeated characters, the first string is:")
    printString(firstStringASCII)
    print ("")
    print ("The second string is:")
    printString(secondStringASCII)






