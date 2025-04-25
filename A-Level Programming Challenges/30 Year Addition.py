correctGuesses = 0
arrGuesses = []
total = 0
incorrect = 0
totalGuesses = 0

while True:
    yearArr = []
    year = str(input("Enter a year: "))
    if len(year) == 4:
        try:
            for i in range (4):
                yearArr.append(int(year[i]))
            break
        except:
            print ("Whoops! not a valid format!")
    else:
        print ("Whoops! not a valid format!")

for i in range (4):
    total = total + yearArr[i]

factors = []
for i in range (1,total+1):
    if total % i == 0:
        factors.append(i)
        
while True:
    while True:
        try:
            guess = int(input("Enter a guess of a factor of the result of the addition: "))
            break
        except:
            print ("Whoops! that was not a valid guess!")
    totalGuesses = totalGuesses + 1
    
    if total % guess == 0 and guess not in arrGuesses:
        print ("Well done! you guessed correctly!")
        correctGuesses = correctGuesses + 1
        arrGuesses.append(guess)
    else:
        print ("Whoops! either that was wrong or you already guessed it!")
        incorrect = incorrect + 1
    if totalGuesses == len(factors):
        print ("Well done! you got all the factors!")
        break
    if incorrect > 2:
        print ("Whoops! you've run out of guesses!")
        break
    
print (f"The total of the year's digits is {total}.")
print (f"You got {correctGuesses}/{len(factors)} points!")