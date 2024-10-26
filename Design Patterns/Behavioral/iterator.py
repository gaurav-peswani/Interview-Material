"""
Iterator Pattern:
 * Lets you traverse elements of  collection without exposing its underlying representation.
"""

import random

class PersonalList:

    def __init__(self):
        self.list = []

    def add(self, element):
        self.list.append(element)

    def remove(self, element):
        self.list.remove(element)

    def __iter__(self):
        # return LinearIterator(self.list)
        return RandomIterator(self.list)
    
class LinearIterator:
    
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == len(self.iterable):
            raise StopIteration
        
        value = self.iterable[self.index]
        self.index += 1
        return value

class RandomIterator:

    def __init__(self, iterable):
        self.iterable = iterable
        self.visited = set()

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.visited) == len(self.iterable):
            raise StopIteration

        random_index = random.randint(0, len(self.iterable) - 1)
        while random_index in self.visited:
            random_index = random.randint(0, len(self.iterable) - 1)
        
        self.visited.add(random_index)
        return self.iterable[random_index]
    
if __name__ == "__main__":
    my_list = PersonalList()
    my_list.add("Item 1")
    my_list.add("Item 2")
    my_list.add("Item 3")
    my_list.add("Item 4")

    for item in my_list:
        print(item)