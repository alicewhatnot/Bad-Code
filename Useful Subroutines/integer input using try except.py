def getInteger(statement : str):
    #Defensive method of asking for an integer
    #Can be tweaked for any data type or range
    while True:
        try:
            userInput = int(input(statement))
            if userInput < 1 or userInput > 4:
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
userInput = getInteger()