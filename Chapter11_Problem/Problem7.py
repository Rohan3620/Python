""" Override the __len__ method on vector of problem 5to display the dimension of the vector. """
"""write a class vector represnting a vector of n
   dimension overload the + and * opertors which
   calculate the sum and dot product of them """
class Vector:
    def __init__(self,l):
        self.l = l
    def  __len__(self):
        return len(self.l)
v1=Vector([1,2,3])
print(len(v1))  