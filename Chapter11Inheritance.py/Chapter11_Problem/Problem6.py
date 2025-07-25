"""write __str__()method to print the vector as follows :
1i,2j,3k"""
class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def __str__(self):
        return f"{self.x}i,{self.y}j,{self.z}k"

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

print("Addition:", v1 + v2)        
print("Dot Product:", v1 * v2)

print("Addition:", v1 + v3)
print("Dot Product:", v1 * v3)
