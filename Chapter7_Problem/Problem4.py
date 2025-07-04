#WAP to find whether a give number is prime or not
number = int(input("Enter a number: "))

# Check if number is less than or equal to 1
if number <= 1:
    print("It is not a prime number")
else:
    # Check for factors
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print("It is not a prime number")
            break
    else:
        print("It is a prime number")        
