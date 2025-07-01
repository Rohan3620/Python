import os

# Ask the user to input a directory path
directory = input("Enter the path of the directory: ")

# Check if the path exists and is a directory
if os.path.isdir(directory):
    print(f"\nContents of '{directory}':")
    for item in os.listdir(directory):
        print(item)
else:
    print("Invalid directory path.")
