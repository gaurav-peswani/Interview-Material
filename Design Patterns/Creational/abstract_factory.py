"""
Abstract Factory Pattern:
 * Provides an interface for creating families of related or dependent objects without
    specifying their concrete classes.
"""
from abc import ABC, abstractmethod

class ProductA(ABC):

    @abstractmethod
    def get_details():
        pass

class ProductB(ABC):

    @abstractmethod
    def get_details():
        pass

class ConcreteProductA1(ProductA):

    def __init__(self):
        self.product_id = "ProductA1"

    def get_details(self):
        return self.product_id
    
class ConcreteProductA2(ProductA):

    def __init__(self):
        self.product_id = "ProductA2"

    def get_details(self):
        return self.product_id
    
class ConcreteProductB1(ProductB):

    def __init__(self):
        self.product_id = "ProductB1"

    def get_details(self):
        return self.product_id
    
class ConcreteProductB2(ProductB):

    def __init__(self):
        self.product_id = "ProductB2"

    def get_details(self):
        return self.product_id
    
class Factory(ABC):

    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass

class ConcreteFactory1(Factory):

    def __init__(self):
        self.create_product_a()
        self.create_product_b()

    def create_product_a(self):
        self.product_a = ConcreteProductA1()

    def create_product_b(self):
        self.product_b = ConcreteProductB1()

    def get_product_details(self):
        print(f"I have the products: {self.product_a.get_details()}, {self.product_b.get_details()}")

class ConcreteFactory2(Factory):

    def __init__(self):
        self.create_product_a()
        self.create_product_b()

    def create_product_a(self):
        self.product_a = ConcreteProductA2()

    def create_product_b(self):
        self.product_b = ConcreteProductB2()

    def get_product_details(self):
        print(f"I have the products: {self.product_a.get_details()}, {self.product_b.get_details()}")

if __name__ == "__main__":
    ConcreteFactory1().get_product_details()
    ConcreteFactory2().get_product_details()
    
