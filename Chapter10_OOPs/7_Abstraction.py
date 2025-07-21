from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

    def sleep(self):
        print("Sleeping... 😴")

class Dog(Animal):
    def make_sound(self):
        print("Bark! 🐶")

class Cat(Animal):
    def make_sound(self):
        print("Meow! 🐱")

# a = Animal()  #Can't instantiate abstract class

d = Dog()
c = Cat()

d.make_sound()
c.make_sound()
d.sleep()
