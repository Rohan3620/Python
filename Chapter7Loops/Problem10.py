#WAP to print multiplication table of n using loop in reverse order
number=int(input("Enter a number : "))
for i in range(1,11):
    print(f"{number}*{11-i}={number*(11-i)}")
print()    
for i in range(10, 0, -1):  # Start from 10 to 1
    print(f"{number} * {i} = {number * i}")
