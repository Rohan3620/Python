# Write a program to insert data into CSV file and display it

data = input("Enter data separated by commas: ")

with open("File.csv", "w+") as f:
    f.write(data)
    f.seek(0)  
    print("Data inside CSV file:")
    print(f.read())
