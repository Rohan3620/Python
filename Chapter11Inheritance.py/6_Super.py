class Employee:
    def __init__(self):
        print("Constructor of Employee : ")
    a = 1

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of Programmer : ")
   
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manger : ")
   
    c = 3

Obj = Manager()
print(Obj.a)  # Inherited from Employee
print(Obj.b)  # Inherited from Programmer
print(Obj.c)  # Defined in Manager
