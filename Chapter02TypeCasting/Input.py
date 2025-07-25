# Full name input
fname = input("Enter First Name: ")
lname = input("Enter Last Name: ")
print("Full name is:", fname + " " + lname)

# Without typecasting (for demonstration)
# it not sum it concadate it as input take as String by default
a = input("Enter 1st number: ")
b = input("Enter 2nd number: ")
print("Sum without typecasting (concatenation):", a + b)

# With typecasting
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print("Sum after typecasting (addition):", a + b)
