students_data = {}

for i in range(3):
    name = input(f"\nEnter the name of student {i+1}: ")
    marks = {}
    
    for subject in ["Math", "Science", "English"]:
        while True:
            try:
                score = int(input(f"Enter marks in {subject} for {name} (0 to 100): "))
                if 0 <= score <= 100:
                    marks[subject] = score
                    break
                else:
                    print("❌ Marks should be between 0 and 100.")
            except ValueError:
                print("❌ Please enter valid numbers only.")
    
    students_data[name] = marks

print("\n🎓 List of Pass Students and Their Percentages:\n")

for student, subjects in students_data.items():
    total_marks = sum(subjects.values())
    percentage = (total_marks / 300) * 100
    passed_all = all(m >= 33 for m in subjects.values())
    
    if passed_all and percentage >= 40:
        print(f"✅ {student} passed with {percentage:.2f}%")

