def setupArrays():
    ''' Makes an easily modifiable copy of the school names and their scores for use inside the program '''
    #here is where the amount of schools and their names should be changed in the program for testing
    schoolNames = ["a","b","c","d","e"]
    schoolScores = [0,0,0,0,0]
    
    #here is where the formatting is stripped to the name and score and split into its parts
    try:
        file = open('matchScores.txt', 'r')
        for line in file:
            parts = line.strip().split(":  ")
            school, winNum = parts
            if school in schoolNames:
                schoolIndex = schoolNames.index(school)
                schoolScores[schoolIndex] = int(winNum)
        return schoolScores,schoolNames
    
    #if the school is not in the file to be split it just returns the default schoolScores array defined at the top of this subroutine
    except:
        return schoolScores,schoolNames
            
def getSchool(schoolNames):
    ''' Takes an input from the user as the school name and checks to see if the school is present in the array of school names '''
    
    while True:
        try:
            userInput = str(input("Enter the school to add the number of wins to: "))
            if userInput not in schoolNames: 
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")

def getWins(schoolScores,school, schoolNames):
    ''' Takes an input from the user as the number of wins then checks the total wins for the school '''
    while True:
        try:
            #finding the school that we want to change the win amount in the array
            schoolIndex = schoolNames.index(school)
            currentWins = schoolScores[schoolIndex]
            
            #accounting for the cases where the total wins would be over 20 and then reasking for input
            if currentWins >= 20:
                print ("They already have 20 wins.")
                return 0
            
            userInput = int(input("Enter the number of wins to add: "))
            
            if userInput < 0:
                print("Wins cannot be negative. Please enter a positive number.")
                continue
            
            if userInput + currentWins > 20:
                print("Sorry, that would bring the win total to over 20.")
                continue
            
            return userInput
        
        except ValueError:
            print("Invalid entry. Please enter an integer.")
        except Exception as e:
            print("Error:", e)

def storeWins(school,wins,schoolNames,schoolScores):
    ''' Again finds which school wins we are changing then adding the wins to the array only if wins is greater than 0 meaning a valid win input'''
    schoolIndex = schoolNames.index(school)
    if wins > 0:
        schoolScores[schoolIndex] = schoolScores[schoolIndex] + wins
    schoolFound = False
    
    #finally updating the school name with the number of wins
    file = open('matchScores.txt', 'r')
    lines = file.readlines()
    
    #this checks to see if the school is already in the file to be updated
    for line_number, line in enumerate(lines):
        if school in line:
            lines[line_number] = (f"{school}:  {schoolScores[schoolIndex]}\n")
            schoolFound = True
            break
        
    #this then appends the school name and win to the bottom of the file if it is not present already
    if schoolFound == False:
        lines.append(f"{school}: {schoolScores[schoolIndex]}\n")
    file = open('matchScores.txt', 'w')
    file.writelines(lines)
    file.close()
            
def enteringData():
    ''' Asks for school name and wins to add then stores them in a file '''
    stopEntry = "n"
    
    while True:
        #here all the functions that have been created above are called in order
        schoolScores,schoolNames = setupArrays()
        school = getSchool(schoolNames)
        wins = getWins(schoolScores,school,schoolNames)
        storeWins(school,wins,schoolNames,schoolScores)
        
        #this leaves the while true to enter data indefinatly
        stopEntry = str(input("Stop entering data? (y to leave) "))
        if stopEntry == "y":
            break

def displayData():
    ''' Outputs all schools in the file by iterating through each line and outputting its contents '''
    try:
        file = open('matchScores.txt', 'r')
        for line in file:
            print (line)
        file.close()
    except:
        print ("Sorry, it appears the text file is not present")
        
def quiting():
    ''' returning True only if the user confirms they want to leave ''' 
    userInput = str(input("Are you sure you want to quit? (y to confirm) "))
    if userInput == "y":
        return True
    
def scoresMenu():
    ''' Using if statements for a case structure of the different inputs defined below '''
    leaving = False
    while True:
        print ("Press 1 to enter and save new data\n"
               "Press 2 to load and display data\n"
               "Press 3 to quit")
        userInput = str(input())
        if userInput == "1":
            enteringData()
        elif userInput == "2":
            displayData()
        elif userInput == "3":
            leaving = quiting()
        else:
            print ("Sorry, that was an invalid input.")
        if leaving == True:
            break
        
#Perhaps the shortest main program ive ever made
scoresMenu()
        

