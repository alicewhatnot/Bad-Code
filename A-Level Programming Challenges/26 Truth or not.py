def truthTable(inputNum):
    variables = [chr(i) for i in range(65, 65 + inputNum)]
    print (" | ".join(variables))
    combinations = 2 ** inputNum
    for i in range (combinations):
        combo = bin(i)[2:].zfill(inputNum)
        print (" | ".join(combo))

def getInteger():
    while True:
        try:
            userInput = int(input("Enter an integer between 2 and 10: "))
            if userInput not in range(2,11):
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
inputNum = getInteger()
truthTable(inputNum)
    
    
