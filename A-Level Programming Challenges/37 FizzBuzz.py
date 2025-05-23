class FizzBuzz():
    def __init__(self,userInput):
        try:
            self.userInput = userInput 
            if self.userInput < 0:
                raise Exception
        except:
            print("Invalid entry.")
        self.userInput = userInput
        self.fizzed = False

    def checkFizz(self):
        if self.userInput % 3 == 0:
            print ("Fizz", end = " ")
            self.fizzed = True
        else:
            return False 
        
    def checkBuzz(self):
        if self.userInput % 5 == 0:
            if self.fizzed == False:
                print ("Buzz", end = " ")
            else:
                print ("Buzz")
        else:
            return False
    
    def checkOops(self):
        prime = True
        for i in range (2, self.userInput):
            if self.userInput % i == 0:
                prime = False
        if prime == True:
            print ("OOPS")
        else:
            return False
                
    def outputNumber(self):
        return self.userInput
    
#MAIN
game = FizzBuzz(15)
fizz = False
buzz = False
oops = False
game.checkFizz()
game.checkBuzz()
game.checkOops()
if [fizz,buzz,oops] == False:
    game.outputNumber()