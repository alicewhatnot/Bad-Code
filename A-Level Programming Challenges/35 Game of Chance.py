import random
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def getInteger(x):
    while True:
        try:
            if x == "a":
                userInput = float(input("Enter your total balance: £"))
            else:
                userInput = float(input("Enter your bet: £"))
                
            if userInput <= 0:
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")

def addBonuses(value):
    #Multiplying based on number bonuses
    number = random.randint(0,30)
    multiplier = 1
    
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
        value = 0
        multiplier = 0
    return value,number,multiplier

def checkBet(account,value):
    return account - value < 0

def checkZero(account):
    return account == 0
    
conditions = {"Even": "2x", "Multiple of 10": "3x", "Prime": "5x", "Below 5": "2x"}
print ("You are betting on a number 0-30")
for conditions, count in conditions.items():
    print (f"{conditions:<15}: {count}")
print ("Rewards stack. Good luck!\n")
balance = getInteger("a")

while True:
    if checkZero(balance):
        print ("You have no money left in your account.")
    bet = getInteger("b")
    if checkBet(balance,bet):
        print ("Sorry, you don't have enough balance.")
        break
    bet,number,multiplier = addBonuses(bet)
    print (f"The number was {number} and you win £{bet} at {multiplier}x.")
    balance = balance + bet
    print (f"Your current balance is {balance}")

#2. Make it remove money from balance
#4. Develop your program to allow multiple bets on different numbers