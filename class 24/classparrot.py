# class parrot
class parrot:
    species = "amazon parrot"
    speciesx = "macaw"
    def __init__(self,age,name):
        self.age = age
        self.name = name
henry = parrot('10','henry')
melisa = parrot('15','melisa')
print("henry is",henry.age , henry.name)
print("melisa is",melisa.age,melisa.name)
print("henry is",henry.speciesx)
print("melisa is",melisa.species)