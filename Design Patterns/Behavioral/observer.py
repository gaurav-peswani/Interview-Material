"""
Observer Pattern:
 * A one to many dependency between objects such that when one of the object changes state, all the other
    objects are notified of that change and updated automatically.
 * Listener, Publisher/Subscriber Model.
"""
from abc import ABC, abstractmethod

class Subject(ABC):
    
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Observer(ABC):

    @abstractmethod
    def update(self):
        pass

class ConcreteSubject(Subject):

    def __init__(self, value):
        self.value = value
        self.observers = []

    def add_observer(self, observer):
        return self.observers.append(observer)
    
    def remove_observer(self, observer):
        return self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_value(self):
        return self.value
    
    def change_value(self):
        self.value += 1
        self.notify()

class ConcreteObserver(Observer):

    def __init__(self, subject):
        self.subject = subject
        self.value = None
        pass

    def update(self):
        self.value = self.subject.get_value()

    def display(self):
        print(f"The value is {self.value}.")

if __name__ == "__main__":

    subject = ConcreteSubject(value=0)

    observer1 = ConcreteObserver(subject=subject)
    observer2 = ConcreteObserver(subject=subject)
    observer3 = ConcreteObserver(subject=subject)

    subject.add_observer(observer1)
    subject.add_observer(observer2)
    subject.add_observer(observer3)

    print()

    subject.change_value()
    observer1.display()
    observer2.display()
    observer3.display()

    print()

    subject.change_value()
    observer1.display()
    observer2.display()
    observer3.display()

    print()

    subject.change_value()
    observer1.display()
    observer2.display()
    observer3.display()


    




