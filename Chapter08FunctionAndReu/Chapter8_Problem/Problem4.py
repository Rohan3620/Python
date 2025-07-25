#WAP recursive function to calulate the sun of n natural number

def sumofNatural(a):
    if(a==1):
        return 1
    return a+sumofNatural(a-1)
number=int(input("Enter a number to find the sum "))
print(f"sum of natural number till {number} is : ",sumofNatural(number))