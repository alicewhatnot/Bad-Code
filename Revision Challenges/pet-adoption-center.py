class Pet():
    def __init__(self,name,species):
        self.name = name
        self.species = species
        
    def getDetails(self):
        return f"{self.name} the {self.species}"
    
class Adopter():
    def __init__(self,adopterName):
        self.adopterName = adopterName
        self.adoptedPets = []
        
    def adoptPet(self,pet):
        self.adoptedPets.append(pet)
    
    def returnPet(self,pet):
        if pet in self.adpotedPets:
            self.adoptedPets.remove(pet)
        else:
            print("you dont own that pet!!")
    
    def listPets(self):
        for pet in self.adoptedPets:
            print (pet.getDetails())
        
    def showStatus(self):
        return self.adopterName

class VIPAdopter(Adopter):
    def __init__(self, adopterName, donationAmount):
        super().__init__(adopterName) 
        self.donationAmount = donationAmount

    def showStatus(self):
        print(f"{self.adopterName} with donation of £{self.donationAmount}")

adopter1 = VIPAdopter("alice","5000")
pet1 = Pet("banana","duck")
adopter1.adoptPet(pet1)
adopter1.listPets()
        