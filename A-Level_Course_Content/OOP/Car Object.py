class Car():
    #Initialiser setting up initial attributes
    def __init__ (self,registration,make):
        self._registration = registration
        self._make = make
        self._mileage = 0
        self._date_of_inspection = "N.D"
    
    #Methods for returning attributes or changing them
    def getRegistration(self):
        return self._registration
    
    def getMake(self):
        return self._make
    
    def getMileage(self):
        return self._mileage
    
    def getDateOfInspection(self):
        return self._date_of_inspection
    
    def setMileage(self):
        self._mileage = getInteger("Enter the mileage: ")
    
    def setDateOfInspection(self):
        self._date_of_inspection = input("Enter the date of inspection: ")

def getInteger(statement):
    #defensive user input
    while True:
        try:
            userInput = int(input(statement))
            if userInput < 0:
                raise Exception
            return userInput
        except:
            print("Invalid entry. Try again")

#Initial car instantiation
registration = "AP21 SSJ"
make = "Volvo"
newCar = Car(registration,make)

#Repeating UI with choices, calls appropriate method
while True:
    print ("Enter 1 to see car details.\n"
           "Enter 2 to change car details.\n")
    userInput = getInteger("")
    if userInput == 1:
        print ("Enter 1 for registration\n"
               "Enter 2 for make\n"
               "Enter 3 for mileage\n"
               "Ender 4 for date of inspection")
        
        userInput = getInteger("")
        if userInput == 1:
            print(newCar.getRegistration())
        elif userInput == 2:
            print(newCar.getMake())
        elif userInput == 3:
            print(newCar.getMileage())
        elif userInput == 4:
            print(newCar.getDateOfInspection())
        else:
            print ("Invalid Entry.")
    elif userInput == 2:
        print ("Enter 1 to change mileage\n"
               "Enter 2 to change date of inspection\n")
        userInput = getInteger("")
        if userInput == 1:
            newCar.setMileage()
        elif userInput == 2:
            newCar.setDateOfInspection()
        else:
            print ("Invalid entry")
    else:
        print ("Invalid Entry")
        

