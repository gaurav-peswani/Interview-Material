"""
Decorator Pattern:
 * Attaches additional responsibilities to and object dynamically (at runtime).
 * Decorators provide a flexible alternative to subclassing for extending functionalities.
 * Caller is the Decorator which is getting the component (base class instantiatiaon) and the calling the component's
    method and then wrapping more data into that inside it's method.
"""
from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def get_description(self):
        pass

class ConcreteComponent(Component):

    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

class Decorator(Component):

    def __init__(self, component):
        self.component = component

    def get_description(self):
        self.component.get_description()

class ConcreteDecorator1(Decorator):

    def get_description(self):
        return f"Decorated the Description ({self.component.get_description()}) as per Decorator 1."
    
class ConcreteDecorator2(Decorator):

    def get_description(self):
        return f"Decorated the Description ({self.component.get_description()}) as per Decorator 2."
    
if __name__ == "__main__":

    component = ConcreteComponent("I am a Concrete Component")

    decorator1 = ConcreteDecorator1(component=component)
    print(decorator1.get_description())

    decorator2 = ConcreteDecorator2(component=decorator1)
    print(decorator2.get_description())
        
