from abc import ABC, abstractmethod

class Shape(ABC):  # abstract base class
    @abstractmethod
    def area(self):  # abstract method
        pass

    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius
obj=Circle(7)
print("Area of circle is : ",obj.area())
print("Perimeter of circle is : ",obj.perimeter())