#WAP a program to print the following star pattern
"""
  * 
 ***
*****
n=3
 """
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(" " * (n - i), end="")      # Decrease spaces as row increases
    print("*" * (2 * i - 1))          # Increase stars in odd numbers
