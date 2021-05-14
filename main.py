import petClass
import dogClass
import catClass
import penClass

pet1 = petClass.pet("Fluffy", "ger")
cat1 = catClass.cat("Katie", "cat", 15, "Angy", True)
dog1 = dogClass.dog("Frankie", "dog", 15, "IDK", "92", "XL")

pen1 = penClass.pen()
pen1.addPets(pet1)
pen1.addPets(cat1)
pen1.addPets(dog1)
pen1.displayPets()