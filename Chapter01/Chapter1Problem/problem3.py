import os
directory = input("Enter the path of the directory: ")
if os.path.isdir(directory):
    print(f"\nContents of '{directory}':")
    for item in os.listdir(directory):
        print(item)
else:
    print("Invalid directory path.")
