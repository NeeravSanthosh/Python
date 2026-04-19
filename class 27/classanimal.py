from abc import ABC, abstractmethod
class Animal(ABC):

    def move (self):
        pass
    
class human(Animal):
    def move(self):
        print("i can walk , jump, sit and run")
class bird(Animal):
    def move(self):
        print("i can fly")
class dog(Animal):
    def move(self):
        print("i can run and rest")
class fish(Animal):
    def move(self):
        print("i can swim")
N = human()
N.move()
N = bird()
N.move()
N = dog()
N.move()
N = fish()
N.move()