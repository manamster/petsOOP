import petClass

class cat(petClass.pet):
    """This is a cat based on the pet but different than the dog"""
    def __init__(self, name, type1, health, mood, claws):
        """This creates all the needed variables for a cat"""
        super(cat, self).__init__(name, type1, health)
        self.mood = mood
        self.claws = claws

    def getMood(self):
        """Gets the cats mood"""
        return(self.mood)

    def getClaws(self):
        """Gets wether the cat has claws or not"""
        return(self.claws)

    def makeSound(self):
        """This makes the cat make a noise"""
        print("Meow")

    def __str__(self):
        """This returns that it is a cat and the name"""
        print("I am a cat and ", end="")
        return super(cat, self).__str__()