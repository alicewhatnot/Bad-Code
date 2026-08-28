class Ford():
    def maker(self):
        print ("made by ford")

class Audi():
    def maker(self):
        print ("made by audi")
        

class Car():
    def __init__(self,object):
        self.type = object
        print ("I am a car")
        
van = Audi()
vehicle = Car(van)
#calling vehice.type which within takes the method arguemnt which is pickup which is made by ford
vehicle.type.maker()