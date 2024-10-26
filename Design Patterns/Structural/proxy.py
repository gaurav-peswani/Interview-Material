"""
Proxy Pattern:
 * Provides a surrogate or placeholder for another object in order to control
    access to it.
 * Used for delayed instantiation, external requests or access control.
"""

from abc import ABC, abstractmethod

class Subject(ABC):

    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):

    def request(self):
        print("Performing Request!")

class Proxy(Subject):

    def __init__(self):
        self.__real_subject = RealSubject()

    def request(self, user_id):
        if user_id < 5:
            print("Request not allowed!")
        else:
            self.__real_subject.request()

if __name__ == "__main__":
    Proxy().request(user_id=1)
    Proxy().request(user_id=5)

