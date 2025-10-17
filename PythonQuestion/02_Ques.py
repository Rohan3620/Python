a=100
b=3.14
c=2+3j
print()
print("Numeric datatype")
print(f"Datatype of {a} is {type(a)}")
print(f"Datatype of {b} is {type(b)}")
print(f"Datatype of {c} is {type(c)}")

print()
a=True
print("Boolean datatype")
print(f"Datatype of {a} is {type(a)}")

print()
a="Rohan"
print("Text sequence datatype")
print(f"Datatype of {a} is {type(a)}")

print()
a=[1,"Rohan",True,1.2]
b=(1,2,3,"Rohan",1.2)
c=range(0,10,2)
print("Sequences datatype")
print(f"Datatype of {a} is {type(a)}")
print(f"Datatype of {b} is {type(b)}")
print(f"Datatype of {c} is {type(c)}")


print()
a = {1, 2, 3}        
b = frozenset([1,2]) 
print("Sets datatype")
print(f"Datatype of {a} is {type(a)}")
print(f"Datatype of {b} is {type(b)}")

print()
a = {"name": "Rohan", "age": 21}
print("Mapping datatype")
print(f"Datatype of {a} is {type(a)}")


a = b'hello'              # bytes, immutable
b = bytearray(b'abc')    # mutable sequence of bytes
c = memoryview(b)       # view on byte data without copying

print()
print("Binary datatype")
print(f"Datatype of {a} is {type(a)}")
print(f"Datatype of {b} is {type(b)}")
print(f"Datatype of {c} is {type(c)}")

a = None
print()
print("None datatype")
print(f"Datatype of {a} is {type(a)}")
