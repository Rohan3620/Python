#write a program to make a copy of text file "this.txt"
# Program to make a copy of text file "this.txt"

# Open the source file in read mode
with open("this.txt", "r") as f:
    # Open the destination file in write mode
    with open("copy.txt", "w") as f1:
        # Copy line by line
        for line in f:
            f1.write(line)
