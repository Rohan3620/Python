""" 
Create a class Employee and add salary 
and increment properties to it.
Write a method salaryAfterIncrement using 
@property decorator and a setter to change 
increment based on the desired salary.
"""

class Employee:
    salary = 234      # Base salary
    increment = 20    # Percentage increment

    @property
    def salaryAfterIncrement(self):
        return self.salary + (self.salary * self.increment / 100)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        self.increment = ((new_salary / self.salary) - 1) * 100

obj = Employee()
print("💰 Salary after increment:", obj.salaryAfterIncrement)

obj.salaryAfterIncrement = 280.8
print(f"🔁 New increment percentage:{obj.increment:2f }")
