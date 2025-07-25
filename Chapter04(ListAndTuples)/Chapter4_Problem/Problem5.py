#WAP to count no of zeros in a list with 5 numbers
MY_List = []
for i in range(5):
    element=int(input("Enter the Element of list : "));
    MY_List.append(element)

print("Number of zero in  List :", MY_List.count(0))
