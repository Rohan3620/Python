""" WAP to greet all the person names stored in list 
l1=["Rohan","Krishna","Mohan","Badal","Harry"]
which start with M 
 """
l1 = ["Rohan", "Mukesh", "Mohan", "Mohit", "Harry"]
for name in l1:
    if name.startswith("M"):
        print("Hello", name)
