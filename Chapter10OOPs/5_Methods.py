class Employee:
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # 🌟 Instance Method:
    # - First parameter is 'self' which refers to the current object
    # - Can access instance variables and class variables
    # - Called using object of the class
    def show(self):
        print(f"{self.name} earns {self.salary} at {Employee.company}")

    # 🌟 Class Method:
    # - Defined using @classmethod decorator
    # - First parameter is 'cls' which refers to the class, not the object
    # - Can access and modify class variables
    # - Can be called using object or class name
    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    # 🌟 Static Method:
    # - Defined using @staticmethod decorator
    # - No 'self' or 'cls' parameter
    # - Does not access or modify instance or class data
    # - Like a normal function inside the class (utility/helper function)
    # - Can be called using class name or object
    @staticmethod
    def greet():
        print("Welcome to the company!")

# 🌟 Creating an object of the class (Instance)
obj = Employee("Rohan", 10000)
obj.show()
# 💼 Calling Class Method via object (changes the class variable)
obj.change_company("Microsoft")

# 👋 Calling Static Method (independent of object or class data)
obj.greet()

# 📋 Calling Instance Method (displays object-specific info + class variable)
obj.show()
