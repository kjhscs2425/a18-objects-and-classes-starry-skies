# -*- coding: utf-8 -*-

class Cat:
    """a cat"""
    def __init__(self, name):
        self.name = name
    def __str__(self):
        # I'm being cute with the emoji here. Delete it if you get errors.
        return f"<a 🐱Cat named {self.name}>"
    def speak(self):
        # I'm being cute with the emoji here. Delete it if you get errors.
        print(f"{self.name} says meow!🐱")

ella = Cat("Ella")
print(ella)

# Write a new class `Dog`.
# Your class should have its own `__init__` method that sets a attribute `name`.
# Your class should have its own `__str__` method that returns a string.
#### YOUR CODE HERE ####
class Dog:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"I'm a cat named {self.name}"
    def speak(self):
        print(f"{self.name} says bark!")
damien = Cat("Damien")
print(damien)