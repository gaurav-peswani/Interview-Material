"""
Strategy Pattern: 
 * [Interfaces inside the Main Class] Turns a set of behaviors into objects and makes them 
    interchangeable inside original context object.
 * Strategy allows the algorithm vary independently from the clients that use it.  
"""
from abc import ABC, abstractmethod

class MainAlgorithm():
    def __init__(self, strategy=None):
        self.strategy  = strategy

    def get_strategy(self):
        return self.strategy
    
    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.validate()
        self.strategy.process()

class Strategy(ABC):
    
    @abstractmethod
    def validate(self):
        pass

    def process(self):
        pass

class Algorithm1(Strategy):

    def __init__(self):
        pass

    def validate(self):
        print("Validating as per Algorithm 1's requirements!")

    def process(self):
        print("Processing as per Algorithm 1's steps!")

class Algorithm2(Strategy):

    def __init__(self):
        pass

    def validate(self):
        print("Validating as per Algorithm 2's requirements!")

    def process(self):
        print("Processing as per Algorithm 2's steps!")

if __name__ == "__main__":
    algorithm = MainAlgorithm()
    
    algorithm.set_strategy(Algorithm1())
    algorithm.execute()

    algorithm.set_strategy(Algorithm2())
    algorithm.execute()