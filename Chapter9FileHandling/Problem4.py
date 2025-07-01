""" 
A file contain a word "Donkey" multiple times.
you need to write a program which replace this word 
with ##### by updating the same file. 
"""
# Open the file in read mode
with open("Donkey.txt") as f:
    data = f.read()

if "Donkey" in data:
    # Open the file in write mode to overwrite it
    with open("Donkey.txt", "w") as f:
        f.write(data.replace("Donkey", "#####"))
    print("Written done") 
else:
    print("Written not done")
