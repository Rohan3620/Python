#WAP to sum a list with 4 numbers
List = []
for i in range(4):
    element = int(input(f"Enter  {i+1}: "))
    List.append(element)
print("Sum of List :", sum(List))
