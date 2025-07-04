# Constructor is a special method that is called when an object is created.
# It is used to initialize the attributes of the class.
# It makes the first call to the class when an object is created.
# It is defined using the __init__() method.
# It takes 'self' as the first parameter, which refers to the instance of the class.

class Employee:
    # Class-level attributes (default values)
    language = "Python"
    salary = 100000
    name = "Harry" 

    # Constructor (dunder method)
    def __init__(self, name, salary, language):
        print("Constructor is called when an object is created.")
        self.name = name
        self.salary = salary
        self.language = language

# Creating the first object
harry = Employee("Harry", 100000, "Python")
print(harry.language, harry.salary, harry.name)

# Creating the second object
rohan = Employee("Rohan", 120000, "Java")
print(rohan.name, rohan.salary, rohan.language)
