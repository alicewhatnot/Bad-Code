import math

def getInteger(statement : str,version : str):
    '''Defensive method of asking for an integer
    Can be tweaked for any data type or range'''
    while True:
        try:
            userInput : int = int(input(statement))
            PUT VERSION CONTROL HERE
            if userInput <= 0:
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
def cosineRule(sideA,sideB,sideC):
    try:
        cosA = (sideA*sideA - sideB*sideB - sideC*sideC)/(-2*sideB*sideC)
        angleA = math.acos(cosA)
        return angleA
    except:
        print ("Invalid triangle.")
        return "ERROR"

while True:
    mode = getInteger("Three sides or two and one angle? (enter a or b): ","a")
    sideA = getInteger("Enter the first side: ","b")
    sideB = getInteger("Enter the second side: ","b")
    sideC = getInteger("Enter the third side: ","b")
    
    if cosineRule(sideA,sideB,sideC) == "ERROR":
        break
    if sideA == sideB == sideC:
        print ("Equilateral.")
    elif cosineRule(sideC,sideA,sideB) == math.pi/2 or cosineRule(sideB,sideC,sideA) == math.pi/2 or cosineRule(sideA,sideB,sideC) == math.pi/2:
        print ("Right-angled.")
    else:
        print ("Scalene")
        
        
#develop to take in two sides and an angle, compute missing angle