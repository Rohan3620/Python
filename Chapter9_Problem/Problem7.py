#WAP to find out the line number  where is present from above question
with open("log.txt", "r") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "Python" in line:
        print("Python found at line", lineno)
        break
    lineno += 1 
else:
    print("Python not found")

  

