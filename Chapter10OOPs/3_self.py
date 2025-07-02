#Self is a reference to the current instance of the class.
#It is not a keyword, but a convention in Python.
#It is used to access variables that belong to the class.
# It is similar to 'this' in Java.
class Employee:
    language="Python" #language is a class attribute
    salary=100000
    def get_info(self): 
       print(f"The language is {self.language}.\nThe Salary is {self.salary}.")
    @staticmethod#use if we not want to use self
    #@staticmethod is used to define a method is decorator
    #that does not require access to the instance or class.
    ##It can be called on the class itself or on an instance of the class.
    def get_greet():
        print("Hello, welcome to the Employee class!")
RohanObj=Employee()
RohanObj.get_info() #it is same as RohanObj.get_info(RohanObj)