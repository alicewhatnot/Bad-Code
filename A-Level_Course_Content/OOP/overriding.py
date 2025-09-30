class Animal:
    def __init__(self,state,size):
        self.state = state
        self.size = size
        
    def feed(self):
        self.size += 1
        print (self.state, "fed")
        
class Fish(Animal):
    def __init__(self,state,size):
        Animal.__init__(self,state,size)
        self.maxSize = 2
    
    def setMaxSize(self,max):
        self.maxSize = max
        
    def feed(self):
        self.size += 2
        print (self.state, "fed")
        if self.size >= self.maxSize:
            self.state = "BIG FISH"
            
thisFish = Fish("litte fish",3)
thisFish.feed()
        