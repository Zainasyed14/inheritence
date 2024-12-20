class Animal:

    def __init__(self , breed , feature ):
        
        self.breed = breed
        self.feature = feature
    def Printinfo(self):
        print( self.breed , self.feature)

class Cat(Animal):
    def __init__(self , breed ,feature , name):
        self.name = name
        super().__init__(breed , feature)
    def printInfo2(self):
        print(self.name)

kittycat = Cat( "British Shorthair" , "Whiskers", "Mano")
kittycat.Printinfo()
kittycat.printInfo2()

