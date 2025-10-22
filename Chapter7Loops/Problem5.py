#WAP to find the sum of 1st n natural number using while loop
number=int(input("Enter a number : "))
sum=0
i=1
while(i<=number):
    sum+=i
    i+=1
print("Sum of n natural number is  :",sum)
