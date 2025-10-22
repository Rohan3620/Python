# Program to demonstrate different operators in Python
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("\nArithmetic operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

print("\nLogical operators:")
print("a and b:", a and b)
print("a or b:", a or b)
print("a != 0:", a != 0)

print("\nRelational operators:")
print("a > b and b < 0:", a > b and b < 0)
print("a >= b or b >= 0:", a >= b or b >= 0)

print("\nMembership operators:")
l = ["Rohan", "Krishna", "Ram", "Ravi"]
print("'Rohan' in list:", "Rohan" in l)

print("\nIdentity operators:")
x = 10
y = 10
print("x is y:", x is y)

print("\nBitwise operators:")
print("a & b (AND):", a & b)
print("a | b (OR):", a | b)
print("a ^ b (XOR):", a ^ b)
print("~a (NOT a):", ~a)
print("a << 1 (Left shift):", a << 1)
print("a >> 1 (Right shift):", a >> 1)
