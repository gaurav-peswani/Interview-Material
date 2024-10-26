"""
Bridge Pattern:
 * Decouple an abstraction from its implementation so that the two can vary independently.
"""

from abc import ABC, abstractmethod

class Abstraction(ABC):

    @abstractmethod
    def do(self):
        pass

class Implemetor(ABC):

    @abstractmethod
    def doFirst(self):
        pass

    @abstractmethod
    def doSecond(self):
        pass

class ConcreteAbstraction1(Abstraction):

    def __init__(self, implementor):
        self.implementor = implementor

    def do(self):
        self.implementor.doFirst()
        self.implementor.doSecond()

class ConcreteAbstraction2(Abstraction):

    def __init__(self, implementor):
        self.implementor = implementor

    def do(self):
        self.implementor.doSecond()
        self.implementor.doFirst()

class ConcreteImplementor1(Implemetor):

    def __init__(self):
        pass
    
    def doFirst(self):
        print("I am doing the addition!")

    def doSecond(self):
        print("I am doing the multiplication!")

class ConcreteImplementor2(Implemetor):

    def __init__(self):
        pass
    
    def doFirst(self):
        print("I am doing the sutraction!")

    def doSecond(self):
        print("I am doing the division!")


if __name__ == "__main__":
    ConcreteAbstraction1(ConcreteImplementor1()).do()
    print()
    ConcreteAbstraction1(ConcreteImplementor2()).do()
    print()
    ConcreteAbstraction2(ConcreteImplementor1()).do()
    print()
    ConcreteAbstraction2(ConcreteImplementor2()).do()

