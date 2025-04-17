# List of student grades
grades = [85, 90, 55, 78, 92, 68, 74]

# Iterate through the list and check the condition
for grade in grades:
    if grade >= 80:
        print(f"Grade {grade}: Pass")
    else:
        print(f"Grade {grade}: Fail")