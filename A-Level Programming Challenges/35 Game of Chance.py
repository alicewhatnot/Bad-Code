import random
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def getInput(x,number):
    while True:
        #Each case, a b or c is for a different instance of getInput and what is required from it (inefficient im sure)
        if x== "c":
            try:
                userInput = int(input("Enter the number of numbers to bet on: "))
                if userInput < 1 or userInput > 10:
                    #Goes to exception even if 'valid' (syntactically not logically) float / int input
                    raise Exception
                return userInput
            except:
                print ("Invalid entry. Must be between 1 and 10 numbers.")
        else:
            try:
                if x == "a":
                    userInput = float(input("Enter your total balance: £"))
                elif x == "b":
                    userInput = float(input(f"Enter your bet for number {number}: £"))
                    
                if userInput <= 0:
                    raise Exception
                return userInput
            except:
                print("Invalid entry. Try again")

def addBonuses(valueArray,amount):
    numberArray = []
    #Multiplying based on number bonuses
    multiplier = 1

    for game in range(amount):
        number = 0
        number = random.randint(0,30)
        while number in numberArray:
            number = random.randint(0,30)
        numberArray.append(number)
        multiplier = 1
        if number % 2 == 0:
            multiplier = multiplier * 2
        if number % 10 == 0:
            multiplier = multiplier * 3
        if number in primes:
            multiplier = multiplier * 5
        if number < 5:
            multiplier = multiplier * 2
        if multiplier == 1:
            multiplier = 0
        valueArray[game] = valueArray[game] * multiplier

    #Totalling profit (or loss)
    valueTotal = 0
    for i in range (len(valueArray)):
        valueTotal += valueArray[i]
    return valueTotal,numberArray

def checkBet(account,values):
    #Checks if account has enough money for all bids
    valueTotal = 0
    for i in range (len(values)):
        valueTotal += values[i]
    return account - valueTotal < 0

def checkZero(account):
    return account == 0

#Initial game instructions
conditions = {"Even": "2x", "Multiple of 10": "3x", "Prime": "5x", "Below 5": "2x"}
print ("You are betting on numbers 0-30")
for conditions, count in conditions.items():
    print (f"{conditions:<15}: {count}")
print ("Rewards stack. Good luck!\n")
balance = getInput("a","")

#Betting loop as long as user has money in the account
while True:
    end = False
    if checkZero(balance):
        print ("You have no money left in your account.")
        break
    numBets = getInput("c","")
    bets = []
    number = 1
    totalBets = 0
    #Inputting all bets
    for i in range (numBets):
        bet = getInput("b",number)
        bets.append(bet)
        totalBets += bet
        number += 1
        if checkBet(balance,bets):
            print ("Sorry, you don't have enough balance.")
            end = True
            break
        
    if end == True:
        break
    #Calling main profit calculating function
    returns,numbers = addBonuses(bets,numBets)
    if returns > 0:
        print (f"The numbers were {numbers} and you win £{returns-totalBets} profit.")
    else:
        print (f"The numbers were {numbers} and you loose £{-1*(returns-totalBets)}.")
    
    #Recalculating and returning balance before the next round
    balance = balance + returns - totalBets
    print (f"Your current balance is {balance}")