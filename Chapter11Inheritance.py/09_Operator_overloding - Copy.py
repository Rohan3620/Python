class Number:
    def __init__(self, n):
        # Initialize the Number object with a value n
        self.n = n

    def __add__(self, num):
        # Overload the + operator to add two Number objects
        return Number(self.n + num.n)

    def __sub__(self, num):
        # Overload the - operator to subtract two Number objects
        return Number(self.n - num.n)

    def __str__(self):
        # Define how to print the Number object
        return str(self.n)

    def __len__(self):
        # Return the value as an integer when len() is called
        return self.n  # Fixed: should return int, not str


# Create Number objects
n = Number(1)
m = Number(2)
o = Number(10)
x = Number(4)

# Demonstrate operator overloading
print(n + m)        # Output: 3
print(m + o)        # Output: 12
print(n - m)        # Output: -1
print(n + m + o)    # Output: 13
print(n - m + o)    # Output: 9
print(n - m + o + x)  # Output: 13

# Demonstrate __len__ usage
print(len(o))       # Output: 10