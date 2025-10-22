# Write a program to find all duplicates in two different lists

l1 = ["Rohan", "Ram", "Ravi"]
l2 = ["Rohit", "Rosan", "Ravi"]

def duplicates(l1, l2):
    common = set(l1) & set(l2)   
    if common:
        print("Duplicate elements found:", common)
    else:
        print("No duplicates found!")

duplicates(l1, l2)
