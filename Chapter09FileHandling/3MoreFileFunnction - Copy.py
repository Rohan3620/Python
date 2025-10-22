st = "Rohan is good boy\n"

f = open("File.txt", "r")
print(f.read())

f = open("File.txt", "r+")
f.write(st)
print(f.read())

f = open("File.txt", "w")
f.write(st)
f = open("File.txt", "w+")
f.write(st)
print(f.read())

st = "Rohan is good \n"
f = open("File.txt", "a")
f.write(st)
f = open("File.txt", "a+")
f.write(st)
print(f.read())
f.close()
