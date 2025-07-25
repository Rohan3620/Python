words=["Donkey","bad","idiot"]
with open("Donkey.txt") as f:
    data = f.read()

for word in words:
    data=data.replace(word,"#####")
with open("Donkey.txt", "w") as f:
    f.write(data)
    print("Written done") 


