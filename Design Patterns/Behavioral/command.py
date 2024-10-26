"""
Command Pattern:
 * Encapsulates a request as an object thereby letting you parametrize other objects with different
   requests, queue or log requests and support undoable operations.
"""

from abc import ABC, abstractmethod

class Command(ABC):

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unexecute(self):
        pass

class ConcreteCommand1(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action1()

    def unexecute(self):
        self.receiver.reverse_action1()

class ConcreteCommand2(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.action2()

    def unexecute(self):
        self.receiver.reverse_action2()

class Receiver():

    def __init__(self):
        pass

    def action1(self):
        print("Performing Action 1.")

    def reverse_action1(self):
        print("Performing Reverse Action 1.")

    def action2(self):
        print("Performing Action 2.")

    def reverse_action2(self):
        print("Performing Reverse Action 2.")

class Invoker():

    def __init__(self):
        self.button1 = None
        self.button2 = None

    def set_button1_command(self, command):
        self.button1 = command

    def set_button2_command(self, command):
        self.button2 = command

    def press_button1(self):
        self.button1.execute()
        self.button1.unexecute()

    def press_button2(self):
        self.button2.execute()
        self.button2.unexecute()

if __name__ == "__main__":

    invoker = Invoker()
    receiver = Receiver()

    command1 = ConcreteCommand1(receiver)
    command2 = ConcreteCommand2(receiver)

    invoker.set_button1_command(command1)
    invoker.set_button2_command(command2)

    invoker.press_button1()
    invoker.press_button2()

