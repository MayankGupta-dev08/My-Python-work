'''
module --> abc

Abstract Class  --> ABCMeta
NOTE - Its is used to create a base class with certain methods which you want that every derived class must consist.
NOTE - We can't directly make the object of the abstract class.

abstract Decorator --> @abstractmethod
NOTE - @abstractmethod, A decorator indicating abstract methods. Requires that the metaclass is ABCMeta or derived from it. A class that has a metaclass derived from ABCMeta cannot be instantiated unless all of its abstract methods are overridden. This tells that any function/method which is decorated with @abstractmethod in Base class is to be mandatorily available in all derived classes of that base class.
'''

from abc import ABCMeta
from abc import abstractmethod

class Shape(metaclass = ABCMeta):
    type = "Parallelogram"
    sides = 4

    @abstractmethod
    def printArea(self):
        return 0

class Square(Shape):
    name = "Square"

    def __init__(self, s):
        self.side = s
        print(f"Shape: {self.name} and it is a {self.type} with {self.sides} sides.")

    def printArea(self):
        return self.side* self.side

class Rectangle(Shape):
    name = "Rectangle"

    def __init__(self, s1, s2):
        self.side1 = s1
        self.side2 = s2
        print(f"Shape: {self.name} and it is a {self.type} with {self.sides} sides.")

    def printArea(self):
        return self.side1* self.side2


sq = Square(4)
print("Area:", sq.printArea(), "\n")
rec = Rectangle(4,8)
print("Area:", rec.printArea())

'''Output
Shape: Square and it is a Parallelogram with 4 sides.
Area: 16 

Shape: Rectangle and it is a Parallelogram with 4 sides.
Area: 32'''