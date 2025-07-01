""" 
Wap to print first n line of the following pattern
* * * *
* * *
* *
* for n=4
"""
def pattern(n):
    for i  in range(n):
        print("* "*(n-i))

number =int(input("Enter a number : "))
pattern(number)