""" 
Create a class pets fron a class Aniaml
and further create class Dog form Pets.
Add a method bark to class Dog.
"""

""" 
Create a class Pets from a class Animal,
and further create class Dog from Pets.
Add a method bark to class Dog.
"""
class Animals:
    def __init__(self):
        print("This is the parent class: Animals")
class Pets(Animals):
    def __init__(self):
        super().__init__()  
        print("This is the parent class of Dog and child class of Animals")
class Dog(Pets):
    def __init__(self):
        super().__init__()  
        print("This is the child class of Pets (and grandchild of Animals)")

    def bark(self):
        print("Dog barks: Woof Woof!")
obj = Dog()
obj.bark()
