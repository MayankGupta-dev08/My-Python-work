'''Simple Inheritance Question'''

class Animal:
    animalType = "Mammal"

class Pet(Animal):
    colour = "White"

class Dog(Pet):
    def __init__(self):
        print("Dog is barking, bhau!! bhau!!")

d = Dog()