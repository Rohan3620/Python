#WAP to rename files 
import os
old_name = "new_filename.txt"
new_name = "Rename.txt"
    
os.rename(old_name, new_name)
print(f"File renamed from {old_name} to {new_name}")
