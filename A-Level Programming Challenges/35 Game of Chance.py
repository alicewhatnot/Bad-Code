import random
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def getInteger():
    while True:
        try:
            userInput = float(input("Enter your bet: £"))
            if userInput <= 0:
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")

conditions = {"Even": "2x", "Multiple of 10": "3x", "Prime": "5x", "Below 5": "2x"}
print ("You are betting on a number 0-30")
for conditions, count in conditions.items():
    print (f"{conditions:<15}: {count}")
print ("Rewards stack. Good luck!\n")


def multiplier(value):
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

bet = getInteger()
bet,number,multiplier = multiplier(bet)
print (f"The number was {number} and you win £{bet} at {multiplier}x.")

#2. Develop your program to store the user’s current balance and stop them from betting if they have no money left
#4. Develop your program to allow multiple bets on different numbers