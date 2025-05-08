import math

def getInteger(statement : str,version : str):
    '''Defensive method of asking for an integer
    Can be tweaked for any data type or range'''
    while True:
        try:
            userInput : int = int(input(statement))
            if version == "a":
                if not(userInput == 1 or userInput == 2):
                    raise Exception
            else:
                if userInput <= 0:
                    raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
def getFloat(statement : str,version : str):
    '''Defensive method of asking for a float
    Can be tweaked for any data type or range'''
    while True:
        try:
            userInput : float = float(input(statement))
            if version == "a":
                if not(userInput == 1 or userInput == 2):
                    raise Exception
            else:
                if userInput <= 0:
                    raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")
            
def cosineRuleSide(sideA,sideB,sideC):
    try:
        cosA = (sideA*sideA - sideB*sideB - sideC*sideC)/(-2*sideB*sideC)
        angleA = math.acos(cosA)
        return angleA
    except:
        print ("Invalid triangle.")
        return "ERROR"
    
def cosineRuleAngle(angleA,sideB,sideC):
    try:
        sideA = math.sqrt(sideB*sideB + sideC*sideC -2*sideB*sideC*math.cos(math.radians(angleA)))
        return sideA
    except:
        print ("Invalid triangle.")
        return "ERROR"

while True:
    mode = getInteger("Three sides or two and one angle? (enter 1 or 2): ","a")
    if mode == 1:
        
        sideA = getInteger("Enter the first side: ","b")
        sideB = getInteger("Enter the second side: ","b")
        sideC = getInteger("Enter the third side: ","b")
        
        if cosineRuleSide(sideA,sideB,sideC) == "ERROR":
            break
        if sideA == sideB == sideC:
            print ("Equilateral.")
        elif cosineRuleSide(sideC,sideA,sideB) == math.pi/2 or cosineRuleSide(sideB,sideC,sideA) == math.pi/2 or cosineRuleSide(sideA,sideB,sideC) == math.pi/2:
            print ("Right-angled.")
        else:
            print ("Scalene")
            
    if mode == 2:
        sideB = getInteger("Enter the one of the sides: ","b")
        sideC = getInteger("Enter the other side: ","b")
        angleA = getFloat("Enter the angle in degrees: ","b")
        sideA = cosineRuleAngle(angleA,sideB,sideC)
        print (f"The third side is {round(sideA,3)} units. (3d.f)")