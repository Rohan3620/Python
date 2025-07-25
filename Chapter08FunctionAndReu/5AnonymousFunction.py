#Basic Anonymous Function
SI = lambda p,r,t: p*r*t # it is single line function
print(SI(100,5,1)) 

# Using lambda with sorted
students = [('Rohan', 85), ('PK', 90), ('Mira', 80)]
students_sorted = sorted(students)
print(students_sorted)

students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)

# Using lambda with map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  
# Using lambda with filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  