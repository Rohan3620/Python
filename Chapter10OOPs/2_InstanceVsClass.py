class Employee:
    language="Python" #language is a class attribute
    salary=100000

RohanObj=Employee()
RohanObj.name="Rohan" # RohanObj.name is an object specific attribute
print(RohanObj.name,RohanObj.language,RohanObj.salary)  
RohanObj.language="Java"
print(RohanObj.name,RohanObj.language,RohanObj.salary)#object attribute more prefernce than class attribute
