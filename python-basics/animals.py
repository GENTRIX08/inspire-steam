#Name : Gentrix Anyango
# Date : 19/02/2026
# Program to show inheritance in python

class Animal():
    def __init__(self,species,weight,food):
        self.species = species
        self.weight = weight
        self.food = food

    def grow(self,weight):
        weight = 1.1 * weight
        print(f"The animal weight{weight} kgs")

    def eat(self,food):
        print("The animal eats {food}")    




class Dog(Animal):
    def __init__(self,species,weight,breed):
        super().__init__(species,weight,food)
        self.colour = colour
        self.weight = weight
        self.breed = breed

def barks(self,barks):
    print(f"The dog says woof woof {bark}")



class horse(Animal):
    def __init__(self,species,weight,food):
        self.species= species
        self.weight= weight
        self.food= food

    def neigh(self,neigh):
        print(f"The animal neighs {neighs}")

    def eat(self,food):
        print(f"The animal eats{food}")