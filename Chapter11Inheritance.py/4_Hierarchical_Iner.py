class Employee:
    company = "ITC"
    
    def show(self):
        print(f"Company: {self.company}")

class Manager(Employee):
    def manager_work(self):
        print("Manages the team.")

class Programmer(Employee):
    def programmer_work(self):
        print("Writes code.")

class Designer(Employee):
    def designer_work(self):
        print("Designs the UI/UX.")

# Creating objects of all child classes
m = Manager()
p = Programmer()
d = Designer()

# All child classes can access the parent class method
m.show()
m.manager_work()

p.show()
p.programmer_work()

d.show()
d.designer_work()
