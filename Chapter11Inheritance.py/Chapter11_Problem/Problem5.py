"""write a class vector represnting a vector of n
   dimension overload the + and * opertors which
   calculate the sum and dot product of them """
class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result=self.x+other.x,self.y+other.y,self.z+other.z
        return result
    def __mul__(self,other):
        result=self.x*other.x+self.y*other.y+self.z*other.z
        return result
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"
v1=Vector(1,2,3)
v2=Vector(4,5,6) 
v3=Vector(7,8,9)           
print("Addition:", v1 + v2  )
print("Dot Product:", v1 * v2)    

print("Addition:", v1 + v3)
print("Dot Product:", v1 * v3)  