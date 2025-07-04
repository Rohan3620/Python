my_set = set()
print("Length of set initially:", len(my_set))    

my_set.add(20)       # int
my_set.add(20.00)    # float (equal to 20, same as above)
my_set.add(20.01)    # float (unique)
my_set.add("20")     # str (unique)

print("Set contents:", my_set)

for item in my_set:
    print(f"{item} is of type {type(item)}")

print("Length of set finally:", len(my_set))    
