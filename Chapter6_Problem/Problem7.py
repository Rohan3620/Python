"""WAP to calculate the grade of the student from his marks
   Schema:
   90-100 = Ex
   80-89 = A
   70-79 = B
   60-69 = C
   50-59 = D
   <50    = E
"""

marks = int(input("Enter the marks of user: "))

if 90 <= marks <= 100:
    print("Grade: Ex")
elif 80 <= marks < 90:
    print("Grade: A")
elif 70 <= marks < 80:
    print("Grade: B")
elif 60 <= marks < 70:
    print("Grade: C")
elif 50 <= marks < 60:
    print("Grade: D")
elif 0 <= marks < 50:
    print("Grade: E")
else:
    print("Invalid marks. Please enter a value between 0 and 100.")
