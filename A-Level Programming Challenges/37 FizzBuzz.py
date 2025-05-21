Fizz Buzz
Create a program that replicates the famous game Fizz Buzz. The program will take an input, e.g. 20, and then print out the list of Fizz Buzz up to and including that number, where:
• Any multiple of 3 is replaced by the word ‘Fizz’
• Any multiple of 5 is replaced by the word ‘Buzz’
• Any multiple of both 3 and 5 is replaced by the word ‘FizzBuzz’
Extension:
1. Replace any prime number with the word ‘OOPS!’
2. Allow the user to enter the base numbers that they want to replace words with. E.g. 2 and 3, which would mean:
• Any multiple of 2 is replaced by the word‘Fizz’
• Any multiple of 3 is replaced by the word‘Buzz’
• Any multiple of both 2 and 3 is replaced by the word‘FizzBuzz’


class FizzBuzz():
    def __init__(self,userInput):
        self.userInput = userInput
        
    def checkInteger(self):
        #Defensive method of asking for an integer            #put this in the constructor to verify at creation
        #Can be tweaked for any data type or range
        while True:
            try:
                self.userInput = int(input(self.userInput))
                if self.userInput < 0:
                    raise Exception
                return self.userInput
            except:
                print("Invalid entry. Try again")
        
    def checkFizz(self):
        if self.userInput % 3 == 0:
            print ("Fizz")
        else return False
            
        
    def checkBuzz(self):
        if self.userInput % 5 == 0:
            print ("Buzz")
        else return False
    
#MAIN
game = FizzBuzz(20)
game.checkInteger
