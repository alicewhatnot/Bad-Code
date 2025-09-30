numbers = [0,0,0,0,0,0,0,0,0,0]

def getChoice():
    while True:
        try:
            userInput = int(input("Press 1 to sort integers or 2 to sort a string: "))
            if userInput == 1 or userInput == 2:
                return userInput
            else:
                raise Exception
        except:
            print("Invalid entry. Try again")

def getString():
    while True:
        try:
            userInput = str(input("Enter a string: "))
            words = userInput.split()
            string = ["" for letter in range (len(words))]
            for i in range (len(words)):
                string[i] = words[i]
            return string
        except:
            print("Invalid entry. Try again")
    
            
def getInteger():
    while True:
        try:
            userInput = int(input("Enter an integer: "))
            return userInput
        except:
            print("Invalid entry. Try again")
            
def getOrder(choice):
    while True:
        try:
            if choice == 1:
                userInput = str(input("Would you like the numbers ascending or descending (asc/desc): "))
            else:
                userInput = str(input("Would you like the letters ascending or descending (asc/desc): "))

            if userInput == "asc" or userInput == "desc":
                return userInput
            else:
                raise Exception
        except:
            print("Invalid entry. Try again")
            
def sortNumbersAsc(numbers):
    for count in range(len(numbers)):
        for i in range(1,len(numbers)):
            if numbers[i] < numbers[i-1]:
                temp = numbers[i]
                numbers[i] = numbers[i-1]
                numbers[i-1] = temp
                
def sortNumbersDesk(numbers):
    for count in range(len(numbers)):
        for i in range(1,len(numbers)):
            if numbers[i] > numbers[i-1]:
                temp = numbers[i]
                numbers[i] = numbers[i-1]
                numbers[i-1] = temp

def ordering(order,numbers):
    if order == "asc":
        sortNumbersAsc(numbers)
    elif order == "desc":
        sortNumbersDesk(numbers)
    else:
        print ("Something went wrong - whoops!")
        
def orderingString(order,string):
    if order == "asc":
        for i in range (len(string)):
            word = list(string[i])
            sortNumbersAsc(word)
            string[i] = word
    elif order == "desc":
        for i in range (len(string)):
            word = list(string[i])
            sortNumbersDesk(word)
            string[i] = word
    else:
        print ("Something went wrong - whoops!")
        
def numbersOutput(numbers,choice):
    order = getOrder(choice)
    ordering(order,numbers)
    for i in range (len(numbers)):
        print (numbers[i],"\t",end="")
        
def lettersOutput(string,choice):
    order = getOrder(choice)
    orderingString(order,string)
    for i in range (len(string)):
        for j in range (len(string[i])):
            print (string[i][j],end="")
        print (" ",end="")
        
choice = getChoice()
if choice == 1:
    for i in range (10):
        numbers[i] = getInteger()
elif choice == 2:
    string = getString()
else:
        print ("Something went wrong - whoops!")

if choice == 1:
    numbersOutput(numbers,choice)
else:
    lettersOutput(string,choice)
