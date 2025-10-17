import os
import shutil
print(f"Current directory : {os.getcwd()}")
os.chdir(r"C:\Users\C9IN\Desktop\coding\Python")
print(f"Changed directory : {os.getcwd()}")
print("Items in this folder:", os.listdir())
if os.path.exists("Rohan"):
    os.rmdir("Rohan")  
    print("Deleted old folder: Rohan")
os.mkdir("Rohan")
print("Created new folder: Rohan")
if os.path.exists("ParentFolder"):
    shutil.rmtree("ParentFolder")  # Deletes folder + its contents
    print("Deleted old folder structure: ParentFolder/ChildFolder")
os.makedirs("ParentFolder/ChildFolder")
print("Created folder structure: ParentFolder/ChildFolder")

os.rename("Rohan", "RohanMishra")
print(os.path.exists("Rohan"))
print(os.path.exists("RohanMishra"))
