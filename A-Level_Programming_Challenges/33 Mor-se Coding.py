morseDict = {
    'A': ".-", 'B': "-...", 'C': "-.-.", 'D': "-..", 'E': ".",
    'F': "..-.", 'G': "--.", 'H': "....", 'I': "..", 'J': ".---",
    'K': "-.-", 'L': ".-..", 'M': "--", 'N': "-.", 'O': "---",
    'P': ".--.", 'Q': "--.-", 'R': ".-.", 'S': "...", 'T': "-",
    'U': "..-", 'V': "...-", 'W': ".--", 'X': "-..-", 'Y': "-.--",
    'Z': "--..", ' ': "|"
}

def getKey(dictionary,target):
    #Iterates through dictionary looking for key based on value
    for key, value in dictionary.items():
        if value == target:
            return key
    return "Not Found"

def toMorse():
    #Word taken in and iterated through
    word = str(input("Enter word(s) to convert to morse: "))
    word = word.upper()
    morseWord = []
    for char in range(len(word)):
        try:
            #Morse lookup
            print (morseDict[word[char]], end = " ")
        except:
            print ("Sorry char(s) entered is unsupported.")
            break
    print ("")
        
def toString():
    word = []
    while True:
        #Key lookup corresponding to letter input
        userInput = str(input("Enter a moorse letter or x to finish: "))
        if userInput == "x":
            break
        else:
            letter = getKey(morseDict,userInput)
            if letter == "Not Found":
                print ("Invalid character")
            else:
                word.append(letter)
    
    #Outputting the word
    print ("The converted word is: ",end="")
    for i in range (len(word)):
        print (word[i], end = "")
    print ("")
    
#Main Code
while True:
    #Handling menu input
    userChoice = str(input("Enter 1 to convert to morse.\n"
                           "Enter 2 to convert to string.\n"
                           "Input: "))
    if userChoice == "1":
        toMorse()
    elif userChoice == "2":
        toString()
    else:
        print("That was neither 1 or 2.")

    
    
