
def checkNum(num):
    if num <= 1:
        return "Not greater than 1"
    
    anyfactors = False
    for factor in range (2, num-1):
        if num % factor == 0:
            anyfactors = True
    
    if anyfactors == True:
        return "Not Prime"
    else:
        return "Is Prime"
            

continuing = "y"
while continuing.lower() == "y":
    userinput = int(input("Enter an integer: "))
    print()
    print (checkNum(userinput))
    print()
    continuing = str(input("Continue? (y/n): "))
    print()
    
    

        
