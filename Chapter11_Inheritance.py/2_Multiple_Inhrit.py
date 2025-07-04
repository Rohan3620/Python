class Employee:
    company = "ITC"
    name = "Rohan"

    def show(self):
        print(f"The name is {self.name} and the Company is {self.company}")

class coder:
    language = "Pyhton"  # ⚠️ Typo: should be "Python"
    
    def printLang(self):
        print(f"Out of all languages, here is your language: {self.language}")

class Programmer(Employee, coder):  # Multiple Inheritance
    company = "ITC Infotech"  # Overrides Employee.company

    def showlang(self):
        print(f"The company is {self.company}, and the programmer is good with {self.language} language")

Obj = Programmer()
Obj.show()         # From Employee
Obj.printLang()    # From coder
Obj.showlang()     # From Programmer
