"""
Template Method Pattern:
 * Defines the skeleton of an algorithm in an operation deferring some steps to subclasses.
 * Lets subclasses redefine certain steps of an algorithm without changing the algorithm
    structure.
"""

from abc import ABC, abstractmethod

class AbstractClass(ABC):

    def template_method(self):
        print("First I call operation1().")
        self.operation1()
        print("Then I call operation2().")
        self.operation2()

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

class ConcreteClassA(AbstractClass):

    def __init__(self):
        pass

    def operation1(self):
        print("Operation 1 by Concrete Class A.")

    def operation2(self):
        print("Operation 2 by Concrete Class A.")


class ConcreteClassB(AbstractClass):

    def __init__(self):
        pass

    def operation1(self):
        print("Operation 1 by Concrete Class B.")

    def operation2(self):
        print("Operation 2 by Concrete Class B.")

if __name__ == "__main__":
    ConcreteClassA().template_method()
    print()
    ConcreteClassB().template_method()

