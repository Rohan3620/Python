class Student:
    course = "BCA"  
    def __init__(self):
        self.name = None
        self.age = None
    def input_data(self):
        self.name = input("Enter name of student: ")
        self.age = input("Enter age of student: ")
    def display(self):
        print(f"Course of student is {Student.course}")
        print(f"Name of student is {self.name}")
        print(f"Age of student is {self.age}")
        
obj = Student()
obj.input_data()
obj.display()
