#Next two are classes of which Car is composed of
class fitEngine():
    def fitting(self):
        print ("engine being fitted")
        
class fitWheels():
    def fitting(self):
        print ("wheels being fitted")
        
class Car():
    def __init__(self):
        #Here in constructor the classes are instansiated
        self.fitEngine = fitEngine() 
        self.fitWheels = fitWheels()
        
    def makeCar(self):
        #Composed of because are used here, without which error occurs
        self.fitEngine.fitting()
        self.fitWheels.fitting()
        print ("car made")

#Instance created
my_car = Car()
my_car.makeCar()