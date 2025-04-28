import random
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def getInput(x):
    while True:
        if x== "c":
            try:
                userInput = int(input("Enter the number of numbers to bet on."))
                if userInput < 1 or userInput > 10:
                    raise Exception
                return userInput
            except:
                print ("Invalid entry. Must be between 1 and 10 numbers.")
        else:
            try:
                if x == "a":
                    userInput = float(input("Enter your total balance: £"))
                elif x == "b":
                    userInput = float(input("Enter your bet: £"))
                    
                if userInput <= 0:
                    raise Exception
                return userInput
            except:
                print("Invalid entry. Try again")

def addBonuses(value,amount):
    numberArray = []
    #Multiplying based on number bonuses
    multiplier = 1
    
    for game in range(amount):
        number = 0
        while number not in numberArray:
            number = random.randint(0,30)
            numberArray.append(number)
        if number % 2 == 0:
            multiplier = multiplier * 2
        if number % 10 == 0:
            multiplier = multiplier * 3
        if number in primes:
            multiplier = multiplier * 5
        if number < 5:
            multiplier = multiplier * 2
    
    #Comparing original value to new to check if zero return
    originalValue = value
    value = value * multiplier
    if originalValue == value:
        value = -1 * value
        multiplier = 0
    return value,numberArray,multiplier

def checkBet(account,value):
    return account - value < 0

def checkZero(account):
    return account == 0
    
conditions = {"Even": "2x", "Multiple of 10": "3x", "Prime": "5x", "Below 5": "2x"}
print ("You are betting on numbers 0-30")
for conditions, count in conditions.items():
    print (f"{conditions:<15}: {count}")
print ("Rewards stack. Good luck!\n")
balance = getInput("a")

while True:
    if checkZero(balance):
        print ("You have no money left in your account.")
        break
    bet = getInput("b")
    if checkBet(balance,bet):
        print ("Sorry, you don't have enough balance.")
        break
    numBets = getInput("c")
    bet,numbers,multiplier = addBonuses(bet,numBets)
    if bet > 0:
        print (f"The numbers were {numbers} and you win £{bet} at {multiplier}x.")
    else:
        print (f"The number was {number} and you loose £{-1*bet}.")
    balance = balance + bet
    print (f"Your current balance is {balance}")

#started adding number of bets to the addBonuses function
#4. Develop your program to allow multiple bets on different numbers