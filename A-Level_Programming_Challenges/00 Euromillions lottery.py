from random import randint
mainFormat = "{:2d} {:2d} {:2d} {:2d} {:2d}"
luckyFormat = "{:2d} {:2d}"
mainNumbers = [0,0,0,0,0]
luckyNumbers = [0,0]


def randMain(mainNumbers):
    i = 0
    while i < 5:
        number = randint(1,50)
        if number not in mainNumbers:
            mainNumbers[i] = number
            i = i + 1
    return mainNumbers

def randLucky(luckyNumbers,mainNumbers):
    i = 0
    while i < 2:
        number = randint(1,12)
        if number not in luckyNumbers and number not in mainNumbers:
            luckyNumbers[i] = number
            i = i + 1
    return luckyNumbers

def getInteger():
    while True:
        try:
            userInput = int(input("Enter an integer between 1 and 6: "))
            if userInput not in range(1, 7):
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again.")
   

userInput = getInteger()
rows = userInput

for i in range (rows):
    randMain(mainNumbers)
    randLucky(luckyNumbers,mainNumbers)
    print (mainFormat.format(mainNumbers[0],mainNumbers[1],mainNumbers[2],mainNumbers[3],mainNumbers[4]),":", end="")
    print (luckyFormat.format(luckyNumbers[0],luckyNumbers[1]))
               


