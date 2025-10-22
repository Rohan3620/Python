with open("Data.csv", "a+") as f:
    d = input("Enter data with comma sep : ")
    f.write(d)
    f.seek(0)        
    d = f.read()
    print("Data of file : ", d)
