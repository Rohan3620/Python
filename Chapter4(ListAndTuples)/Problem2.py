marks = []

for i in range(6):
    mark = int(input(f"Enter marks {i+1}: "))
    marks.append(mark)

marks.sort()  # Sort after collecting all marks
print("Marks of students in sorted order:", marks)
print("Max marks of student:", max(marks))
print("Min marks of student:", min(marks))



