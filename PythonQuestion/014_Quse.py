with open("File.txt", "r") as f:
    data = f.read()
words = data.split() 
print(f"Number of words in file: {len(words)}")
