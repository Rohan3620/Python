#WAP to calculate the factorial of a given number for loop
number=int(input("Enter a number to find factorial : "))
i=1
fac=1
while(i<=number):
    fac*=i
    i+=1
print("Factorial of the number : ",fac)    