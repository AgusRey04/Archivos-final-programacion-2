from abc import ABC, abstractclassmethod
class Animal(ABC):
    @abstractclassmethod
    def mover(self):
        pass
    @abstractclassmethod
    def comer(self):
        print("Animal come")

class Gato(Animal):
    def mover(self):
        print("Mover gato")
    
    def comer(self):
        super().comer()
        print('Gato come')

g = Gato()
g.mover()
g.comer()
