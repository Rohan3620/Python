""" 
WAP to genrate multiplication tables from 2 to 20 and write it to diferent 
files 2 to 20 and write it to the different files . Place there files in 
folder.Place these files in a folder for a 13year-old
"""
import os

if not os.path.exists("tables"):
    os.mkdir("tables")

for j in range(2, 21):  # Tables from 2 to 20
    filename = f"tables/table_{j}.txt"  # Save inside 'tables' folder
    with open(filename, "w") as file:
        for i in range(1, 11):  # Multipliers from 1 to 10
            file.write(f"{j} * {i} = {j * i}\n")
    print(f"Table of {j} saved to '{filename}'.")


    
