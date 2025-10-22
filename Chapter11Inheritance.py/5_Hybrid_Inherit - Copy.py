class Employee:
    company = "ITC"

    def show(self):
        print("I am an employee at", self.company)

class Manager(Employee):
    def manage(self):
        print("I manage the team.")

class Programmer(Employee):
    def code(self):
        print("I write code.")

class TeamLead(Manager, Programmer):
    def lead(self):
        print("I lead both managers and programmers.")
lead = TeamLead()
lead.show()       # Inherited from Employee
lead.manage()     # From Manager
lead.code()       # From Programmer
lead.lead()       # Own method
