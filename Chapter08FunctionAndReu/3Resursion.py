def factorial(n):
    if(n==1 or n==0):
        return 1   
    return n*factorial(n-1) 
number=int(input("Enter a number : "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of number {number} is : {factorial(number)}")

