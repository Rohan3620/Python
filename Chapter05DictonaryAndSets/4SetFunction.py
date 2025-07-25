my_set = {1, 2, 3, 4, 4, 1, 1, 1, 1, 1, "Rohan", "Rohan"}
print("Element of set never repeat:", my_set)  # Set automatically removes duplicates
print("Datatype of this is:", type(my_set))

my_set.add("Ram")
my_set.add(10)
print("Element of set after add:", my_set)

my_set.remove("Rohan")
print("Element of set after remove:", my_set)

print("Set length:", len(my_set))

my_set.pop()  # Removes a random element (since sets are unordered)
print("Element of set after pop:", my_set)

my_set.update([100,"Mohan"])# use for adding more than element
print("Set after update : ",my_set)

my_set.discard(4)
print("Set after discard : ",my_set)

print("Shallow copy of set ",set.copy(my_set))

print("Is Mohan in set ","Mohan" in my_set )
print("Is Mohan in not set ","Mohan" not in my_set )

my_set.clear()
print("Element after clear:", my_set)
