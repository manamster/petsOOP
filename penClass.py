import petClass
import catClass
import dogClass

class pen(object):
    """This is the pen that holds all the pets"""
    def __init__(self):
        """Creates the pen list"""
        self.pets = []

    def addPets(self, otherPet):
        """Adds pets to the pen"""
        if len(self.pets) == 0:
            self.pets.append(otherPet)
        else:
            i = 0
            for item in self.pets:
                if otherPet.compareTo(item) <= 0:
                    self.pets.insert(i, otherPet)
                    return
                i+=1
    
    def displayPets(self):
        """"""
        for i in range(len(self.pets)):
            print(self.pets[i])