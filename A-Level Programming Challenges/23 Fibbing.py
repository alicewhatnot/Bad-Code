def fibbing(fibonacci,amount):
    for i in range (amount):
        if i > 1:
            num = fibonacci[i-1]+fibonacci[i-2]
            fibonacci.append(num)
        elif i == 0:
            fibonacci.append(0)
        elif i == 1:
            fibonacci.append(1)

def getInteger():
    while True:
        try:
            userInput = int(input('Enter the number of terms in the sequence you would like to see (1-15): '))
            if userInput not in range(1,16):
                raise Exception
            return userInput
        except:
            print('Invalid entry. Try again')

def reversing():
    while True:
        try:
            userInput = str(input('Would you like to reverse the order they are shown? (y/n): '))
            if userInput == 'y' or userInput == 'n':
                return userInput
            else:
                raise Exception
        except:
            print('Invalid entry. Try again')

def printing(wantsReverse):
    if wantsReverse == 'y':
        for i in range (len(fibonacci)-1,-1,-1):
            print (fibonacci[i],'\t',end='')
    else:
        for i in range (len(fibonacci)):
            print (fibonacci[i],'\t',end='')

def total(fibonacci):
    print ('')
    while True:
        try:
            userInput = input('Would you like a total (y/n): ')
            if userInput == 'y':
                total = 0
                for i in range (len(fibonacci)):
                    total = total + fibonacci[i]
                print (f'The total of the first {len(fibonacci)} in the fibonacci sequence was {total}.')
                return
            elif userInput == 'n':
                return
            else:
                raise Exception
        except:
            print('Invalid entry. Try again')

fibonacci = []
userInput = getInteger()
amount = userInput
fibbing(fibonacci,amount)
wantsReverse = reversing()
printing(wantsReverse)
total(fibonacci)

