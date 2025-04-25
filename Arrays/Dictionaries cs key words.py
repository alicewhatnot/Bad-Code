keywords = {}

def addItem (keywords,repeat):
    while repeat == True:
        keyword = input("Enter the keyword: ")
        definition = input("Enter the definition: ")
        keywords[keyword] = definition
        wantRepeat = input("Enter to add another or x to cancel: ")
        if wantRepeat == "x":
            repeat = False
    
def outputAllKeywords (keywords):
    for key, value in keywords.items():
        print (key,": ",end="")
        print (value)

def outputOneKeyword (keywords,repeat):
    repeat = True
    while repeat == True:
        keyword = input("Enter the keyword you want the definition for: ")
        try:
            print (f"The definition of {keyword} is {keywords[keyword]}")
        except:
            print ("Sorry, your input was not understood")
        wantRepeat = input("Enter to output another or x to cancel: ")
        if wantRepeat == "x":
            repeat = False
    
def deleteKeyword (keywords,repeat):
    repeat = True
    while repeat == True:
        keyword = input("Enter the keyword you want to delete: ")
        try:
            del keywords[keyword]
        except:
            print ("Sorry, your input was not understood")
        wantRepeat = input("Enter to delete another or x to cancel: ")
        if wantRepeat == "x":
            repeat = False
    
while True:
    userInput = str(input(
        "Enter 1 to add a keyword \n"
        "Enter 2 to output all keywords \n"
        "Enter 3 to output one keyword \n"
        "Enter 4 to delete a keyword \n"))
    if userInput == "1":
        repeat = True
        addItem(keywords,repeat)
    elif userInput == "2":
        outputAllKeywords(keywords)
    elif userInput == "3":
        repeat = True
        outputOneKeyword(keywords,repeat)
    elif userInput == "4":
        repeat = True
        deleteKeyword (keywords,repeat)
    else:
        print ("Sorry, your input was not understood.")
        
    