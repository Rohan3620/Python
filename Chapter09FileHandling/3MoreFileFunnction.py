f=open("File.txt")
lines=f.readlines()#it return list each element is line of file
print(lines,type(lines))
lines1=f.readline()
print(lines1,type(lines1))
lines2=f.readline()
print(lines2,type(lines2))
f.close()