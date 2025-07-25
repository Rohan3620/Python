class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")
obj=Employee()
obj.a=45
obj.show()