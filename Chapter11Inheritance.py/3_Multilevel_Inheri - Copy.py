class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

Obj = Manager()
print(Obj.a)  # Inherited from Employee
print(Obj.b)  # Inherited from Programmer
print(Obj.c)  # Defined in Manager
