class Employee:
    language="Python" #language is a class attribute
    salary=100000

RohanObj=Employee()
RohanObj.name="Rohan" # RohanObj.name is an object specific attribute
print(RohanObj.name,RohanObj.language,RohanObj.salary)  

HarryObj=Employee()
HarryObj.name="harry"
print( HarryObj.name, HarryObj.language, HarryObj.salary)  

#Here name is object specific attribute, while language and salary are class attributes.
#We can also access class attributes using the class name.