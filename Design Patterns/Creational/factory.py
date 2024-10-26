"""
Factory Pattern:
 * Defines an interface for creating an object but lets the subclasses decide which class to instantiate.
"""

from abc import ABC, abstractmethod

class Product(ABC):

    @abstractmethod
    def get_details(self):
        pass

class Creator(ABC):

    @abstractmethod
    def create_product(self):
        pass


class ConcreteProductA(Product):

    def __init__(self, details):
        self.details = details

    def get_details(self):
        return self.details

class ConcreteProductB(Product):

    def __init__(self, details):
        self.details = details

    def get_details(self):
        return self.details
    
class ConcreteCreator1(Creator):

    def __init__(self):
        self.product = None
        self.create_product()

    def create_product(self):
       self.product = ConcreteProductA("Product A")

    def get_product_details(self):
        print(f"Product details are: {self.product.get_details()}")
    
class ConcreteCreator2(Creator):

    def __init__(self):
        self.product = None
        self.create_product()

    def create_product(self):
       self.product = ConcreteProductB("Product B")

    def get_product_details(self):
        print(f"Product details are: {self.product.get_details()}")

if __name__ == "__main__":

    creator = ConcreteCreator1()
    creator.get_product_details()

    creator = ConcreteCreator2()
    creator.get_product_details()
    

        
