"""
Adapter Pattern:
 * Converts the interface of a class into another interface the client expects. Lets classes work
    together that couldn't otherwise due to incompatible interfaces.
 * Useful for 3rd party integrations.
"""

from abc import ABC, abstractmethod
import traceback

class Client():

    def __init__(self, target=None):
        self.target = target

    def process(self):
        self.target.request()

class Target(ABC):

    @abstractmethod
    def request(self):
        pass

class Adaptee():

    def __init__(self):
        pass

    def specific_request(self):
        print("Performing the Specific Request() via Adapter.")

class CompatibleTarget(Target):

    def __init__(self):
        pass

    def request(self):
        print("Hey I am compatible!")

class Adapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()

if __name__ == "__main__":
    client = Client()

    client.target = CompatibleTarget()
    client.process()
    print()
    
    try:
        client.target = Adaptee()
        client.process()
    except Exception:
        print(traceback.format_exc())
        print()

    client.target = Adapter(adaptee=Adaptee())
    client.process()
    print()

    # Client ----- can only call ----> Target.request() 
    #   ---- instead it is calling the ----> (Adapter) ---- who is calling ----> Adaptee