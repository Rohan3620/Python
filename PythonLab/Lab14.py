# Write a Python Program that takes a text
# file  as input and return the number of 
# words of a given text file

with open("File.txt","r")as f:
    print("Number of word ",len(f.read().split( )))
