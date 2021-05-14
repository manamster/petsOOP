import petClass

class dog(petClass.pet):
    """This is the dog pet it is similair but different from just a pet"""
    def __init__(self, name, type1, health, breed, weight, size):
        super(dog, self).__init__(name, "dog", health=health)
        self.breed = breed
        self.weight = weight
        self.size = size

    def getBreed(self):
        """Returns the breed of the dog"""
        return(self.breed)

    def getWeight(self):
        """Returns the weight of the dog"""
        return(self.weight)

    def getSize(self):
        """Returns the size of the dog"""
        return(self.size)
    
    def makeSound(self):
        """The dog makes a sound"""
        print("Woof")

    def __str__(self):
        print("I am a dog and ", end="")
        return super().__str__()