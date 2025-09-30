class Language:
    def greeting(self):
        raise NotImplementedError("Subclass must be implemented")
    
class English(Language):
    def greeting(self):
        print ("Hello xxoxo")

class French(Language):
    def sayingHi(self):
        print ("Bonjour")
        
alice = English()
piere = French()

alice.greeting()
piere.greeting()