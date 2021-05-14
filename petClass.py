class pet(object):
    """This is the base class that all pets are derived from"""
    def __init__(self, name, type1, health = 10):
        """Makes the beginning values for all pets"""
        self.name = name
        self.type = type1
        self.health = health
    
    def getName(self):
        """Gets the name"""
        return(self.name)

    def getType(self):
        """Gets the type of pet"""
        return(self.type)
    
    def compareTo(self, otherPet):
      """returns -1 if less than, 0 if equal, 1 if greater than"""
      if self.type < otherPet.getType():
        return(-1)
      elif self.type > otherPet.getType():
        return(1)
      else:
        return(0)

    def getHealth(self):
        """Gets the health of the pet"""
        return(self.health)

    def __str__(self):
        """Returns the name of the pet"""
        string = "my name is " + str(self.name)
        return(string)