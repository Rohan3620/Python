#WAP to print Multiplication table of a given number using while loop
number=int(input("Enter a number : "))
i=1
while(i<=10):
    print(f"{number}*{i}={number*i}")
    i+=1;