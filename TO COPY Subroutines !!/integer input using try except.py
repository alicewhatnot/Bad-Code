def getInteger():
    while True:
        try:
            userInput = int(input("Enter an integer between 1 and 15: "))
            if userInput not in range(1,16):
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
userInput = getInteger()