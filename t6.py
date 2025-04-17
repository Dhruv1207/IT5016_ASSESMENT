# 1. Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# 2. Create a dictionary with student information
students_info = {
    'John': {'age': 20, 'grade': 85},
    'Mary': {'age': 22, 'grade': 90},
    'Lucy': {'age': 21, 'grade': 55},
    'James': {'age': 23, 'grade': 78},
    'Sarah': {'age': 19, 'grade': 92}
}

# 3. Use a while loop to print all numbers in the list
num = 1
print("Numbers from 1 to 10:")
while num <= 10:
    print(num)
    num += 1

# 4. Use a for loop to print a message for each student in the dictionary
print("Student Information")
for name, info in students_info.items():
    print(f"Student: {name}, Age: {info['age']}, Grade: {info['grade']}")

    # 5. Check if the student's grade is greater than or equal to 80
    if info['grade'] >= 80:
        print(f"Pass")
    else:
        print(f"Fail")