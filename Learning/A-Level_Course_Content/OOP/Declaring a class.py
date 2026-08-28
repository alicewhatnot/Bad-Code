class Animal: 
    def __init__ (self,s,n):
        '''Constructing the animal'''
        self.state = s
        self.size = n
        
    def feed(self):
        '''Feed the animal'''
        self.size = self.size + 1
        if self.size == 5:
            self.state = "FISH"
            
    def getState(self):
        '''Return the state of the animal'''
        return self.state
    
    def getSize(self):
        '''Return the size of the animal'''
        return self.size
    
thisFish = Animal("Fish",1)

print (f"{thisFish.getState()} is of size {thisFish.getSize()}") 

while thisFish.getState() != "FISH":
    thisFish.feed()

print (f"It is now a big {thisFish.getState}")
    

    







    